#!/usr/bin/env python3
"""Rebuild index.html (the page served at /cav) from the Google Docs export CAV_paper.html.

Run this after re-exporting the paper from Google Docs:
    cd cav && python3 build.py

Google Docs exports two kinds of <img>:
  - figures: wrapped in a fixed-size `overflow: hidden` span that CROPS them, with
    an inline pixel width on the <img>. Those get scaled up and capped.
  - inline equations: a bare <img> with no style. Those are left completely alone.
"""
import re, sys, pathlib

SRC   = pathlib.Path("CAV_paper.html")
OUT   = pathlib.Path("index.html")
TITLE = ("Interpretable, reusable concept directions in "
         "biological foundation model embedding spaces")

SCALE      = 1.8461   # Google Docs exports at a 624px column; this fills ~900px
MAX_WIDTH  = 900.0
MAX_HEIGHT = 900.0

STYLE = (
    '<style>'
    'body.doc-content{max-width:900px;width:auto;padding:48px 32px;margin:0 auto;'
    'box-sizing:content-box}'
    'body.doc-content img{max-width:100%}'
    # neutralise the fixed-size crop wrapper Google Docs puts around each figure
    'body.doc-content span[style*="overflow: hidden"]{display:block!important;'
    'width:auto!important;height:auto!important;overflow:visible!important;'
    'transform:none!important;margin:0!important}'
    # figures only (inline equations are bare <img> and are not matched here)
    'body.doc-content span[style*="overflow: hidden"] img{display:block;'
    'max-width:min(900px,94vw);height:auto!important;'
    'margin-left:50%!important;transform:translateX(-50%)!important}'
    '@media (max-width:1000px){'
    'body.doc-content{max-width:100%;padding:24px 16px;box-sizing:border-box}'
    'body.doc-content span[style*="overflow: hidden"] img{max-width:100%;'
    'margin-left:0!important;transform:none!important}}'
    '</style>'
)

def scale_figure(tag):
    w = re.search(r'width: *([0-9.]+)px', tag)
    h = re.search(r'height: *([0-9.]+)px', tag)
    if not (w and h):            # bare <img> = inline equation, leave as-is
        return tag, None
    w, h = float(w.group(1)) * SCALE, float(h.group(1)) * SCALE
    k = min(1.0, MAX_WIDTH / w, MAX_HEIGHT / h)
    w, h = w * k, h * k
    tag = re.sub(r'width: *[0-9.]+px',  'width: %.2fpx'  % w, tag, count=1)
    tag = re.sub(r'height: *[0-9.]+px', 'height: %.2fpx' % h, tag, count=1)
    return tag, (w, h)

def main():
    if not SRC.exists():
        sys.exit("missing %s" % SRC)
    s = SRC.read_text(encoding="utf-8")

    old = '<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type">'
    if not s.startswith(old):
        sys.exit("unexpected export format - check the <head> of %s" % SRC)
    s = ('<!doctype html>\n<html lang="en"><head>'
         '<meta content="text/html; charset=UTF-8" http-equiv="content-type">'
         '<meta name="viewport" content="width=device-width, initial-scale=1">'
         '<title>' + TITLE + '</title>' + STYLE + s[len(old):])

    sizes = []
    def repl(m):
        tag, size = scale_figure(m.group(0))
        if size:
            sizes.append((re.search(r'src="([^"]+)"', tag).group(1), size))
        return tag
    s = re.sub(r'<img[^>]*>', repl, s)

    OUT.write_text(s, encoding="utf-8")
    print("wrote %s" % OUT)
    for i, (src, (w, h)) in enumerate(sizes, 1):
        print("  figure %d  %-22s %4.0f x %4.0f" % (i, src, w, h))

main()

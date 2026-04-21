---
permalink: /
title: ""
excerpt: "McWhite Lab"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## McWhite Lab

We develop computational approaches to understand protein function, evolution, and organization — with a focus on interpretability of large language models of biomolecules and gene expression.

**Areas of Research**: Protein language model interpretability, agentic programming, algorithms for bioinformatics, systems biology, proteomics, evolution

---

## Recent News

{% for item in site.data.news %}
**{{ item.date }}** — {{ item.authors }}, "{% if item.url != "" %}<a href="{{ item.url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}", *{{ item.venue }}*, {{ item.pages }}

{% endfor %}

---

## Lab Members

**Principal Investigator**

Claire McWhite, Ph.D. — Assistant Professor, Department of Molecular and Cellular Biology, University of Arizona

**Graduate Students**

- Samuel Love
- Robert Shaw
- Ahmad Shamail


---

#### Contact

clairemcwhite@arizona.edu  
Department of Molecular and Cellular Biology  
The University of Arizona

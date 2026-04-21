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

## Consulting

Claire McWhite is available for consulting in protein language models, single-cell sequencing analysis, and bioinformatics.

**Protein language model expertise includes:**
- Interpreting and applying pretrained protein language models (ESM, ProtTrans, etc.)
- Using protein language model embeddings to assess functional similarity
- Concept activation vectors for automated motif localization in embedding space
- Multiple sequence alignment leveraging protein language models
- Applying protein language models to novel biological questions

Please reach out at clairemcwhite@arizona.edu.

---

#### Contact

clairemcwhite@arizona.edu  
Department of Molecular and Cellular Biology  
The University of Arizona

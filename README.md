# Predicting Multidimensional Research Impact using LLMs and Impact-Augmented Knowledge Graphs

This repository contains the full codebase and evaluation pipeline for the paper *"Predicting Multidimensional Research Impact: A Neurosymbolic Approach using LLMs and Impact-Augmented Knowledge Graphs"*.

We introduce a neurosymbolic framework that models research impact as a structured progression through five semantic stages:

**Reach → Engagement → Feedback → Influence → Outcome**

Rather than relying on traditional metrics like citation counts or attention scores, Flowmetrics captures the evolving and multidimensional nature of research impact. The framework is implemented via an **impact-augmented knowledge graph**, built from arXiv metadata enriched with platform-level signals—such as tweets, citations, and policy mentions.

Large Language Models (LLMs) are prompted using structured evidence from this graph to infer and order impact trajectories between topic pairs.

---

## Objectives

- Model research impact as a **semantic flow across five stages**, moving beyond static, single-score indicators.
- Build an **impact-augmented knowledge graph** combining topic co-occurrence, shared concepts, and platform metrics (Altmetric, CrossRef, arXiv).
- Use **LLMs guided by structured prompts** to predict impact stages and infer progression paths for research topics.
- Evaluate model outputs across:
  - **Stage-level accuracy and F1**
  - **Sequence-level logical coherence**
  - **Cross-model consistency and agreement**

---

## 📂 Repository Structure

```bash
predicting-multidimensional-research-impact/
├── data/
│   └── impact_augmented_kg.ttl              # Serialized KG with platform scores and concept links
│   └── flowmetrics-predictions.csv          # Output from classification stage
├── experiments/
│   ├── Flowmetrics-KG-construction.ipynb        # Builds the impact-augmented knowledge graph (RDF/Turtle)
│   ├── Flowmetrics-LLM-classification.ipynb     # Applies LLMs to predict impact stages for each topic pair
│   ├── Flowmetrics-validation.ipynb             # Evaluates stage-level and sequence-level predictions
│   ├── config.py
│   └── utils.py
├── requirements.txt
└── README.md
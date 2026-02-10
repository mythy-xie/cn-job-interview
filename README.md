# AI-Related Job Interview Guide

> The main content of this code repository is in Chinese.

> This repository may not be suitable for beginners.

## Introduction

This repository serves as a comprehensive, deep-dive study guide and knowledge base for **AI-related Engineer** interviews in 2026 and beyond landscape. 

Moving beyond traditional machine learning "trivia," this project focuses on the **LLM-Native** era, emphasizing the intersection of **Algorithm Design**, **System Efficiency (SysML)**, and **Large-Scale Engineering**. It covers the theoretical foundations, modern architectures, and practical deployment strategies required for modern AI roles.

## Roadmap & Syllabus

The content is planned to be organized into six core modules, designed to bridge the gap between academic theory and industrial application.

### 1. Foundations: Math & ML Core
* **Probability & Statistics:** Bayesian Inference, Variational Inference (VI), MCMC.
* **Optimization:** Second-order methods, Distributed Optimizers (Lion, Sophia), Loss Landscapes.
* **Classical ML at Scale:** Distributed Tree Models (XGBoost/LightGBM), SVM Duality.

### 2. Modern Deep Learning Architectures
* **Transformer Anatomy:** Self-Attention optimization, RoPE/ALiBi, Pre-Norm vs. Post-Norm.
* **Beyond Transformer:** SSMs (Mamba), Linear Attention, Sparse Attention.
* **Efficient Architectures:** Mixture of Experts (MoE), Routing mechanisms.

### 3. LLM Specialization (The Core)
* **Pre-training:** Data pipelines, Deduplication strategies, Scaling Laws (Chinchilla), Mixed-precision training.
* **Post-training & Alignment:** SFT, RLHF (PPO), DPO (Direct Preference Optimization), KTO.
* **Inference:** KV Cache optimization (PagedAttention), Speculative Decoding, Quantization (AWQ/GPTQ).

### 4. AI Infrastructure & SysML
* **Distributed Training:** 3D Parallelism (Data, Tensor, Pipeline), ZeRO Stages, FSDP.
* **Hardware Aware:** GPU Memory hierarchy, Kernel fusion, FlashAttention internals.
* **Serving:** High-throughput serving systems, Continuous batching.

### 5. Domain Specifics
* **Recommender Systems:** Two-tower models, MMoE/PLE, LLM4Rec, Graph Neural Networks.
* **Multimodal:** CLIP alignment, Vision Transformers (ViT), LMM Architectures (LLaVA, Flamingo).
* **Agents:** Tool use, Planning (ReAct/CoT), RAG Systems (Vector DBs, Reranking).

### 6. System Design & Engineering
* End-to-end ML System Design cases.
* Safety, Evaluation, and Red Teaming.

## Tech Stack & Tools

* **Languages:** Python, C++ (CUDA)
* **Frameworks:** PyTorch, JAX
* **Libraries:** Hugging Face Transformers, Deepspeed, Megatron-LM, vLLM, LangChain
* **Ecosystem:** Kubernetes, Ray, Docker

## How to Use

Each directory corresponds to a module above and contains:
- **Concept Notes:** Deep dives into the "Why" and "How".
- **Code Snippets:** Minimal implementations of core algorithms (e.g., Manual Backprop, Attention from scratch).
- **Interview Q&A:** Common pitfalls and high-frequency questions for 2026.

## License

This project is open source and available under the GPL-3.0 License.

## Contribution & Contact

Issues and PRs are welcome if you find any kind of errors or have suggestions for new topics!


> **Note:** This is a living document, updated as I progress through my review from first principles to state-of-the-art implementation details.

---
*Created by [@mythy-xie](https://github.com/mythy-xie) | 2026*
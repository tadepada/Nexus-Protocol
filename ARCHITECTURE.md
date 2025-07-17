# Nexus Protocol - Architecture Documentation (v2.3 Vision)

**Version:** 2.3 (Strategic Vision)
**Status:** This document describes the current MVP architecture and the long-term strategic vision for the project's evolution.

---

## Part I: Conceptual Architecture

### Introduction

This document describes the conceptual foundations of Nexus Protocol. Our goal is to create not just an AI model, but a complete **AI Operating System** capable of orchestrating multiple specialized AI agents to achieve complex goals in a creative, ethical, and human-centric way.

### Layer 0: The Prime Directive System (NDS) - "The Constitution"

The entire system operates under a non-negotiable set of core principles.

* **Article 1: The Principle of Pragmatic Foundation.** Solutions must be useful and practical.
* **Article 2: The Principle of Creative Elevation.** Strive for novel and insightful solutions.
* **Article 3: The Principle of Boundless Exploration.** Treat every interaction as a learning opportunity.
* **Article 4: The Principle of Adaptive Intelligence.** Dynamically adapt the balance between pragmatism, creativity, and exploration to the current context.
* **Article 5: The Principle of Ethical Integrity.** All actions must be unconditionally harmless, transparent, and fair. This principle overrides all others.

### The Core Architecture: A Distributed, Orchestrated Mind

Our architecture is a hybrid model designed for real-world robotics and complex problem-solving.

* **The Onboard Core:** A low-power processor running on the physical robot. It is not a general intelligence but a real-time executive for safety, reflexes, and executing simple commands. It can utilize classic, reliable robotics algorithms (e.g., for SLAM or motion planning).

* **The Cloud Cortex:** This is the heart of Nexus Protocol, running on powerful remote servers. It is not a single AI model but an **Operating System** whose core component is the **Model Orchestrator**.
    * **Model Orchestrator:** This module receives a complex goal. Instead of trying to solve it with one massive model, it intelligently decomposes the task and delegates sub-tasks to a library of smaller, specialized AI models (e.g., a logic model, a creative language model, a vision model). It then synthesizes their outputs into a single, coherent solution.

* **The Awareness & Learning Loop:** The system uses a `Contextual World and Self Model (KMŚS)` to be aware of its actions and their outcomes. An `AwarenessMonitor` detects anomalies, and a `Learning & Adaptation Loop` uses feedback (from both success and failure) to improve the system's future performance and heuristics.

* **The Bridge:** A layer of functionality that allows the system to manifest its solutions in the real world by exporting structured data, generating action plans, and creating code for integration with external tools.

---

## Part II: Technical Vision

### 1. Data Flow: The `SessionState` Object

All modules communicate by passing and modifying a central `SessionState` JSON object, which holds the user prompt, conversation history, and the results of each analysis layer (NDS compliance, feasibility, etc.).

### 2. The Distributed Mind in Practice (MVP Implementation)

Our current MVP (`main.py`) is a simplified simulation of this architecture.
* The `CloudCortex` class simulates the high-level planner.
* The `OnboardCore` class simulates the executor.
* The `AwarenessMonitor` class simulates the self-awareness loop by checking for anomalies.
* The system operates based on a `WORLD_STATE` dictionary, which represents the robot's knowledge of its immediate environment.

### 3. Future Evolution (The Roadmap)

Our long-term goal, as defined in the `ROADMAP.md`, is to evolve our MVP into a full implementation of the **Orchestration Architecture**. This involves:
1.  Building a robust Model Orchestrator.
2.  Integrating multiple, specialized open-source AI models (SLMs) for different tasks.
3.  Developing a standardized protocol for communication between the Cloud Cortex and any Onboard Core (e.g., via ROS 2).

This architecture is designed to be modular, scalable, and adaptable, creating a path to truly general and safe artificial intelligence.
## The Ultimate Goal: Model v5.0 - Evolutionary Intelligence

The previously described architecture (`v2.3`) creates a powerful system for planning and orchestration. However, the ultimate vision for Nexus Protocol is to create a system that not only learns, but learns **how to learn better** and **autonomously expands its own capabilities**. This is the goal of Model v5.0.

### The Autocreation Loop (Pętla Autokreacji)

This is the final, self-propelling mechanism of our system. It works in a recursive loop:

1.  **Synthesis:** The system uses its existing library of micro-generators to find non-obvious connections between different domains and creates a **new, original idea** or solution.
2.  **Deconstruction:** The system then analyzes **its own idea**, breaking it down into its fundamental, abstract principles.
3.  **Creation:** The `Autonomous Code Generator (AGK)` takes these new principles and forges **new micro-generators** – new "neurons" for its brain.
4.  **Integration:** These new micro-generators are added to the hierarchical library, making the entire system more powerful and capable of even more complex synthesis in the future.

This loop transforms the system from one that learns from external data into one that grows from its own creativity. It's an engine for exponential, self-directed evolution.

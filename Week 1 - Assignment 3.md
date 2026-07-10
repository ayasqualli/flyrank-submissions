---
type: Assignment
track: "[[General AI Fluency]]"
week: 1
phase: Setup
status: 🟢 Complete
tags:
date: 2026-07-09
name: AI Workflow Audit & Tool Setup
---

# Assignment: FL-01 Workflow Audit

##  Meta & Objectives

- **Why it matters:** You cannot improve a workflow you have never mapped. Knowing where AI helps, where it wastes your time, and where it should never be trusted is the core fluency skill; everything else builds on this audit.
    
- **The Brief:** Audit 10–15 recurring tasks from my real week, classify how AI should or should not be involved, set up the required AI toolkit, configure one Claude Project, and choose three target tasks to reuse in FL-02 through FL-04.
    

---

##  The Deliverables

### Deliverable Component 1: Workflow Audit Table

|#|Recurring task from my real week|Classification|Rationale|
|---|---|---|---|
|1|Debug backend/API errors in RAG microservices, ADK agents, or Docker services|Collaborate with AI|AI can interpret logs and suggest likely fixes, but I must test the fix locally and verify the architecture.|
|2|Write or polish professional emails in French or English|Delegate to AI with review|AI helps with tone, grammar, and structure, but I review every message before sending.|
|3|Analyze cybersecurity/CTF binaries and challenges|Collaborate with AI|AI can suggest tools, commands, and hypotheses, but the solution must be validated through evidence.|
|4|Decide whether an exploit, vulnerability, or CTF solution is correct|Just me|Final correctness depends on runtime behavior, proof, and ethical judgment, not AI confidence.|
|5|Summarize research papers related to AI, cybersecurity, RAG, or graph learning|Collaborate with AI|AI can simplify and structure the paper, but I need to verify the claims against the source.|
|6|Build project architecture prompts for coding agents like Codex|Collaborate with AI|AI helps structure requirements, but I define the real constraints, priorities, and expected behavior.|
|7|Generate boilerplate code, API routes, UI components, or config files|Delegate to AI with review|This saves time on repetitive implementation, but the code still needs testing and adaptation.|
|8|Review security-sensitive code or authentication logic|Just me|AI can miss subtle authorization, trust-boundary, or data-flow issues, so I must verify them manually.|
|9|Create notes from technical learning sessions or tutorials|Delegate to AI with review|AI can organize messy notes, but I check that the technical meaning remains accurate.|
|10|Translate technical or administrative text between French and English|Delegate to AI with review|AI is useful for translation, but I review formality, context, and exact wording.|
|11|Track project tasks and next steps for side projects|Collaborate with AI|AI can turn messy notes into a plan, but I choose priorities based on deadlines and real constraints.|
|12|Reformat reports, proposals, or documentation into Markdown or LaTeX|Delegate to AI with review|AI improves formatting and clarity, but I verify the technical content and final structure.|
|13|Search for documentation, papers, or tools for a new technical topic|Collaborate with AI|AI can narrow the search space, but I must verify sources, dates, and relevance.|
|14|Run repetitive checks such as linting, formatting, tests, or basic log scans|Fully automate|These are rule-based checks that can be scripted or handled by CI pipelines.|
|15|Decide final claims in academic or professional deliverables|Just me|I am responsible for accuracy, evidence, and ethics, so final claims must come from my judgment.|

---

### Deliverable Component 2: Toolkit Setup Evidence

| Tool              | Setup status                                                                      | Evidence to attach                                     |
| ----------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------ |
| ChatGPT           | Account configured and used for study, coding, writing, and research support      | ![[Attachments/Week 1 - Assignment 3-1783687667001.webp\|222x542]] |
| Claude            | Account created and one Claude Project configured                                 | ![[Attachments/Week 1 - Assignment 3-1783687750250.webp]]          |
| Anthropic Academy | Enrolled in “AI Fluency: Framework & Foundations” and completed at least Module 1 | ![[Attachments/Week 1 - Assignment 3-1783687814203.webp]]          |

---

### Deliverable Component 3: Claude Project Configuration

> **Project name:** Cybersecurity, AI & Research Assistant

> **Custom instructions:**

I am a computer science engineering student and cybersecurity researcher working on AI, machine learning, RAG systems, CTFs, reverse engineering, and software engineering projects.

Use a clear, direct, and practical tone. Prefer concise explanations, but give enough technical detail when debugging code, security issues, or research papers. When helping with code, prioritize correctness, security, and testability. When helping with writing, keep the tone professional, natural, and not overly formal.

Current goals:

- Improve my AI fluency and use AI responsibly in real workflows.
    
- Build and debug RAG-based and agentic software projects.
    
- Improve cybersecurity research workflows, especially reverse engineering, malware analysis, and CTF problem solving.
    
- Produce stronger technical documentation, project prompts, and research summaries.
    
- Save time on repetitive writing, formatting, and debugging tasks while keeping human review for critical decisions.
    

Important rules:

- Do not invent facts, results, references, or code behavior.
    
- Clearly separate assumptions from verified information.
    
- For cybersecurity work, focus on ethical research, defensive learning, and CTF/lab contexts.
    
- Give step-by-step reasoning when debugging, but avoid unnecessary long explanations.
    
- When something is security-sensitive or high impact, remind me what I need to verify manually.
    

---

### Three Target Tasks and Success Definitions

|Target task|Why I chose it|Done well means|
|---|---|---|
|Debugging RAG or agentic project errors|This appears often in my current side projects and wastes time when logs are unclear.|I can provide logs and context to AI, get a likely root cause, test the fix locally, and document the final solution in under 30 minutes for common errors.|
|Summarizing and extracting useful ideas from research papers|I regularly read papers for AI, cybersecurity, RAG, and graph learning.|The output includes the paper’s problem, method, contribution, limitations, and relevance to my project, with no unsupported claims.|
|Writing professional French/English emails and project updates|I often need to communicate with professors, housing services, teammates, and organizers.|The final message is clear, polite, context-aware, grammatically correct, and ready to send after my review in less than 10 minutes.|

---

### Summary for #track-fluency Intro Thread

For FL-01, I audited recurring tasks from my real week as a computer science engineering student working on cybersecurity, AI/ML, RAG systems, CTFs, research, and technical writing.

The main pattern I noticed is that AI is most useful as a collaborator for debugging, research understanding, architecture planning, and CTF reasoning. However, it should not be trusted blindly for final security decisions, exploit correctness, or academic claims. I marked several tasks as “just me” because they require evidence, responsibility, and manual verification.

My three target tasks for the next modules are:

1. Debugging RAG/agentic project errors.
    
2. Summarizing and extracting value from research papers.
    
3. Writing professional French/English emails and project updates.
    

I also set up my AI toolkit with ChatGPT, Claude, and Anthropic Academy, enrolled in AI Fluency: Framework & Foundations, completed the first module, and created a Claude Project with custom instructions based on my goals, tone preferences, and safety requirements.

---

##  AI Collaboration Log

- **Initial Draft / Thought Process:**
    
    - I started by listing the recurring tasks I actually do during the week: debugging projects, reading papers, working on CTF/security tasks, writing emails, formatting documents, and managing side-project plans.
        
    - My first instinct was to mark many tasks as “collaborate with AI,” but I needed to separate low-risk productivity tasks from high-risk judgment tasks.
    
- **The Friction Points:**
    
    - The main challenge was being honest about where AI should not be trusted.
        
    - Security-sensitive work, exploit validation, and final academic claims cannot be delegated because they require proof, evidence, and personal responsibility.
        
    - Another friction point was making the success definitions measurable instead of vague.
    
- **Refinements Made:**
    
    - I added more specific task descriptions based on my actual work in cybersecurity, RAG systems, AI/ML, and student communication.
        
    - I marked at least two tasks as “just me” and explained why.
        
    - I rewrote the three target tasks so each has a measurable “done well” definition that can be reused in FL-02 through FL-04.

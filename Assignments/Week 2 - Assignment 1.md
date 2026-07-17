---
type: Assignment
track: "[[General AI Fluency]]"
week: 2
phase: Foundations
status: 🟢 Complete
tags:
  - voicecard
  - frame
  - portfolio
  - cta
date: 14/07/2026
name: "Frame it as Cases: Work That Speak for Itself"
---
# Frame it as Cases: Work that speaks for itself

## Voice card

direct, honest, technical, plain, no buzzwords

## Standing instruction for AI drafting

Use this voice card for everything you draft for me: direct, honest, technical, plain, no buzzwords.

Use short sentences. Keep my words when possible. Do not write generic portfolio language. Avoid phrases like “passionate,” “results-driven,” “dynamic,” “leveraged,” or “cutting-edge” unless I actually said them.

Write like a real technical person explaining their work to someone who might hire me, collaborate with me, or trust me with serious technical work.

## Audience

The main audience is someone who might hire me, give me an internship, collaborate with me, or review my technical work.

## One action

Check the project, read the case, and contact me if the work fits what they need.

---

# Bio copy

I am a computer science engineering student focused on cybersecurity, AI, and data-intensive systems.

I like projects where the system has to actually work: a backend that responds, an agent that uses the right context, a reverse engineering workflow that follows evidence, or a dashboard that helps people understand what is happening.

My work usually sits between software engineering and security. I build APIs, analyze systems, work with data, and document the decisions behind the result.

I am currently looking for internship and research opportunities in AI, cybersecurity, backend engineering, and applied data systems.

## Short bio version

Computer science engineering student focused on cybersecurity, AI, backend systems, and applied data work. I build practical systems and explain the decisions behind them.

## Contact / CTA copy

Want to work together, review one of my projects, or discuss an internship opportunity?

Contact me by email or check my GitHub.

---

# Case 1: Tiny Go backend

## The problem

The assignment was simple on purpose: build the smallest possible backend with two JSON endpoints, call it from curl and the browser, then publish it on GitHub.

The point was not to build a large app. The point was to understand the request-response loop from the server side and prove that I could publish working code cleanly.

## What I did and decided

I chose Go with `net/http`.

I could have used Node.js or Python, but I wanted to practice something lower-level and simple. Go also makes it clear what the server is doing: define routes, handle requests, return JSON, and listen on a port.

I kept the backend small. No framework. No database. No extra structure that the assignment did not need.

The main decisions were:

- use Go’s standard library instead of a framework;
    
- create two JSON endpoints;
    
- test the endpoints with curl;
    
- make the browser response easy to inspect;
    
- keep the repository clean enough to submit.
    

## What came of it

I ended with a small backend that answers real HTTP requests and can be tested from both the terminal and browser.

The useful part was seeing that a backend does not need to be mysterious. A server receives a request, runs a handler, and sends a response.

I also practiced publishing the work to GitHub, which matters because the repository is part of the submission, not an afterthought.

## Next time

I would add a simple README with exact run commands, endpoint examples, and screenshots of the curl/browser tests.

## CTA

View the repository and run the server locally.

---

# Case 2: AI notes assistant

## The problem

I wanted a way to ask questions over my own notes instead of searching manually through files.

The goal was simple: ask something like “What notes do I have about reverse shells?” and get an answer grounded in the notes, with sources.

The hard part was not only calling an AI model. The hard part was making the system retrieve the right context, pass it correctly to the model, and fail clearly when something breaks.

## What I did and decided

I worked on a backend that receives a user question, retrieves relevant notes, and sends the context to an AI model.

The system had to handle:

- user questions;
- note retrieval;
- source tracking;
- model calls;
- runtime errors;
- clean API responses.

I also had to make decisions around the model provider. The first setup expected Anthropic through Portkey, but that failed because of an API key issue. Since I had Gemini available, I decided to switch toward Gemini instead of forcing a provider I could not use.

One important lesson was that AI errors are not always “AI quality” problems. Sometimes the issue is configuration, missing keys, unexpected response shapes, or backend assumptions like trying to call `.filter()` on something undefined.

## What came of it

The project helped me understand AI integration as a real backend problem.

The model is only one part. The system also needs routing, error handling, retrieval, response formatting, and debugging.

The useful outcome was not just getting an answer from an LLM. It was learning how to make the backend explain what failed when the AI runtime does not behave as expected.

## Next time

I would add stronger validation around model responses before processing them, plus a fallback path when one provider fails.

## CTA

Check the repo and look at how the backend handles AI, retrieval, and errors.

---

# Case 3: Portfolio website

## The problem

I needed a portfolio that does more than list projects.

A portfolio should help a stranger understand what I build, what decisions I make, and why the work is worth trusting. If the page only has project names, screenshots, and icons, it does not explain enough.

## What I did and decided

I worked on the portfolio structure, project framing, and small UI details.

The main decision was to frame projects as cases instead of just cards. Each case needs to show:

- the problem;
- what I did and decided;
- what came of it.

I also worked on the social/profile section. I added profile links like CTFtime and Hack The Box, but Bootstrap Icons did not include those brand icons directly. So I used image-based icons instead and styled them to match the site.

I wanted the page to feel technical but not overloaded. The goal was to make it easy for someone to check my GitHub, CTF profiles, and project work quickly.

## What came of it

The portfolio became clearer and more useful.

It now points people toward the work that matters: projects, repositories, security profiles, and contact information.

The small details also mattered. Fixing the icons, links, spacing, and copy made the page feel more finished.

## Next time

I would add a short case page for each major project, with a repo link, screenshots, and what I would improve next.

## CTA

Visit the portfolio, check the project cases, and follow the links to GitHub, CTFtime, and Hack The Box.

---

# Case 4: CTF and reverse engineering work

## The problem

CTF challenges are not solved by guessing. They require evidence.

In reverse engineering, pwn, forensics, and crypto, the first answer is often wrong. The work is about forming a hypothesis, testing it, and adapting when the output does not match.

## What I did and decided

I worked through challenges using an evidence-first process.

For reversing, that meant looking at control flow, functions, memory behavior, and comparisons. For pwn, it meant testing input behavior, leaks, offsets, and exploit assumptions. For forensics, it meant working with disk images, logs, browser artifacts, registry traces, and file system evidence.

I tried to avoid full plans that ignore new evidence. The better workflow was incremental:

1. inspect one thing;
    
2. record what it proves;
    
3. choose the next action from that evidence.
    

## What came of it

This process helped me work more clearly under uncertainty.

It also improved how I explain technical findings. Instead of only saying “the binary is vulnerable” or “the artifact contains evidence,” I can explain what I saw, why it matters, and what step follows from it.

My CTF work also gave me practical experience with low-level systems, debugging, exploitation, and forensic investigation.

## Next time

I would document solved challenges faster, while the reasoning is still fresh.

## CTA

Read my writeups or check my CTF profiles.

---

# Case 5: HPC monitoring dashboard

## The problem

HPC systems generate a lot of operational information, but that information is not always easy to read or act on.

Users and administrators need to understand resource usage, job status, and system behavior without digging through raw command outputs every time.

## What I did and decided

I worked on a monitoring system using a backend and frontend approach.

The idea was to collect relevant cluster information, expose it through an API, and display it in a dashboard. The system used backend logic to communicate with the HPC environment and frontend components to make the information readable.

The main decisions were:

- separate data collection from display;
    
- keep the backend responsible for system communication;
    
- make the frontend focused on clarity;
    
- show useful operational information instead of raw noise.
    

## What came of it

The project helped turn system-level information into something easier to understand.

It also gave me experience connecting infrastructure, APIs, authentication, and frontend display in one workflow.

## Next time

I would add stronger alerting and historical analysis, so the dashboard does not only show the current state but also helps detect patterns over time.

## CTA

View the dashboard case and technical architecture.

---

# Case 6: Machine learning resource recommender

## The problem

Choosing computing resources is often messy.

For data or HPC workloads, users may not know how much CPU, GPU, RAM, or time they need. Bad estimates can waste resources or make jobs fail.

## What I did and decided

I worked on an ML-based recommender for computing resources.

The goal was to use workload information to suggest appropriate resources. This required thinking about the input features, the target recommendation, and how the model would be useful in a real environment.

I treated the model as part of a system, not just a notebook. The recommendation had to make sense to a user and fit the way compute resources are requested.

## What came of it

The project helped me connect machine learning with operational constraints.

It was not only about model accuracy. It was about whether the recommendation could help someone make a better decision before launching a job.

## Next time

I would improve the evaluation with real workload history and compare the model recommendations against human choices and actual job outcomes.

## CTA

Read the ML case and review the resource recommendation approach.

---
# Case 7: Go bookstore API

## The problem

A backend API is not only routes and JSON.

It also needs to behave correctly when several users make requests at the same time. That means thinking about concurrency, shared state, and safe access.

## What I did and decided

I built a bookstore API in Go.

The useful part was working with goroutines and mutexes. I had to think about what happens when multiple requests touch the same data.

I kept the API focused on backend behavior: routes, handlers, data structures, and concurrency safety.

## What came of it

The project gave me practical experience with Go backend development and concurrent request handling.

It also helped me understand why concurrency bugs are not always visible in small tests. The system may work once, then fail when many requests arrive together.

## Next time

I would add persistent storage, integration tests, and load testing results.

## CTA

View the API repository and backend notes.

---

# Before / After

## Generic AI line

“I am a passionate and results-driven developer who leverages cutting-edge technologies to create innovative solutions.”

## My edited version

“I build practical systems, explain the decisions behind them, and keep the work honest.”

## Why the edited version is better

The generic line could describe anyone. It uses filler words and does not prove anything.

The edited version sounds closer to how I actually want to present my work. It is shorter, clearer, and easier to trust.

---

# Final contact section

## Let’s connect

I am open to internships, research work, and technical collaborations in cybersecurity, AI, backend engineering, and applied data systems.

The best way to judge my work is to read the cases, check the repositories, and look at the decisions behind each project.

If the work fits what you need, contact me.
# Day 42 - GitHub Actions Runners

## What is a GitHub-Hosted Runner?
GitHub ki apni virtual machine hoti hai jo GitHub manage karta hai.
Har job ke liye fresh machine milti hai, kaam khatam toh machine delete.

## What is a Self-Hosted Runner?
Apni khud ki machine jo GitHub ke saath connect hoti hai.
Tu khud manage karta hai.

## Pre-installed Tools (ubuntu-latest)
- Docker
- Python
- Node.js
- Git

## Why Pre-installed Tools Matter?
Time bachta hai - tools install nahi karne padte.
Pipeline fast chalti hai.

## Runner Labels
Labels se specific runner ko target kar sakte hain.
Example: runs-on: [self-hosted, linux, my-linux-runner]

## Comparison Table

| Feature | GitHub-Hosted | Self-Hosted |
|---|---|---|
| Who manages? | GitHub | Aap khud |
| Cost | Free (public repo) | Apni machine ka cost |
| Pre-installed tools | Bahut saare | Khud install karo |
| Good for | Normal CI/CD | Custom hardware, private network |
| Security | Safe (fresh VM) | Dhyan rakhna padta hai |

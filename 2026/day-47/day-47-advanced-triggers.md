# Day 47 – Advanced Triggers: PR Events, Cron Schedules & Event-Driven Pipelines 🚀

## Overview
Today I explored advanced GitHub Actions triggers and built event-driven CI/CD pipelines using:
- Pull Request lifecycle events
- PR validation checks
- Scheduled workflows (cron jobs)
- Path & branch filters
- Workflow chaining with `workflow_run`
- External triggers with `repository_dispatch`

---

## Task 1: Pull Request Lifecycle Events

### Workflow: `pr-lifecycle.yml`

```yaml
name: PR Lifecycle

on:
  pull_request:
    types: [opened, synchronize, reopened, closed]

jobs:
  pr-events:
    runs-on: ubuntu-latest
    steps:
      - name: Print PR Details
        run: |
          echo "Event: ${{ github.event.action }}"
          echo "Title: ${{ github.event.pull_request.title }}"
          echo "Author: ${{ github.event.pull_request.user.login }}"
          echo "Source: ${{ github.head_ref }}"
          echo "Target: ${{ github.base_ref }}"

      - name: Run only if merged
        if: ${{ github.event.pull_request.merged == true }}
        run: echo "PR merged successfully"

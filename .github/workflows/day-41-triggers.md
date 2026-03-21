# Day 41 – Triggers & Matrix Builds

## Task 1: PR Trigger ✅
- File: pr-check.yml
- Trigger: pull_request on main

## Task 2: Schedule Trigger ✅
- Cron midnight: 0 0 * * *
- Cron Monday 9AM: 0 9 * * 1

## Task 3: Manual Trigger ✅
- File: manual.yml
- Input: environment (staging/production)

## Task 4: Matrix Build ✅
- OS: ubuntu + windows
- Python: 3.10, 3.11, 3.12
- Total jobs: 6

## Task 5: Fail-Fast ✅
- fail-fast: true  = ek fail hone pe sab band
- fail-fast: false = ek fail hone pe baaki chalte rahen
- Ubuntu + 3.10 deliberately fail kiya
- Baaki 5 jobs chalte rahe

# Day 47 – Advanced Triggers

## Task 1: PR Lifecycle
Created a workflow that triggers on pull request lifecycle events:
- opened
- synchronize
- reopened
- closed

It prints:
- event type
- PR title
- PR author
- source branch
- target branch

It also has a conditional step that runs only when the PR is merged.

## Task 2: PR Validation Workflow
Created a PR checks workflow that:
- fails if any file is larger than 1 MB
- fails if branch name does not start with `feature/`, `fix/`, or `docs/`
- warns if PR body is empty

## Task 3: Scheduled Workflows
Created a scheduled workflow with:
- `30 2 * * 1` → every Monday at 2:30 AM UTC
- `0 */6 * * *` → every 6 hours

Also added `workflow_dispatch` for manual testing.

### Cron expressions
- Every weekday at 9 AM IST: `30 3 * * 1-5`
- First day of every month at midnight: `0 0 1 * *`

### Why scheduled workflows may be delayed or skipped
GitHub may delay or skip scheduled workflows on inactive repositories or during heavy platform load.

## Task 4: Path & Branch Filters
Created workflows that:
- run only when files in `src/` or `app/` change
- skip when only markdown or docs files change
- run only on `main` and `release/*` branches

### paths vs paths-ignore
- `paths` is used when workflow should run only for specific file changes
- `paths-ignore` is used when workflow should skip for specific file changes

## Task 5: workflow_run
Created:
- `tests.yml` → runs on every push
- `deploy-after-tests.yml` → runs only after `Run Tests` completes

Deployment proceeds only if the test workflow succeeded.

## Task 6: repository_dispatch
Created a workflow that responds to external event type `deploy-request`.

This can be useful when an external system like:
- Slack bot
- monitoring tool
- deployment dashboard
- custom app

needs to trigger a GitHub Actions pipeline.

## workflow_run vs workflow_call
- `workflow_call` is used to reuse one workflow inside another workflow.
- `workflow_run` is used to trigger one workflow after another workflow finishes.

## Screenshot
Add screenshot of PR checks running on a pull request here.

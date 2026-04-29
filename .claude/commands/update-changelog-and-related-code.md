---
name: update-changelog-and-related-code
description: Workflow command scaffold for update-changelog-and-related-code in automatic.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-changelog-and-related-code

Use this workflow when working on **update-changelog-and-related-code** in `automatic`.

## Goal

Updates CHANGELOG.md alongside code or configuration changes to document updates.

## Common Files

- `CHANGELOG.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit relevant code/configuration files
- Update CHANGELOG.md with description of the change

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.
---
name: add-or-update-reference-image
description: Workflow command scaffold for add-or-update-reference-image in automatic.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-or-update-reference-image

Use this workflow when working on **add-or-update-reference-image** in `automatic`.

## Goal

Adds a new reference image (e.g., model cover) and updates the reference metadata JSON.

## Common Files

- `models/Reference/*.jpg`
- `html/reference.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add new image file to models/Reference/
- Update html/reference.json with new entry

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.
# Invariant tests (read-only to the agent)

Tests in this directory encode non-negotiable system properties. The agent may ADD files
here only when a roadmap task says so; it may never modify or delete existing ones.
CI rejects diffs that touch these files without a human-approved label.

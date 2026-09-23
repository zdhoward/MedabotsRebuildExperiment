---
name: Bug report
about: Report wrong behavior in the engine, specs, or blog
title: "[bug] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Bugs found by readers are recorded in BACKLOG.md by the agent and
        promoted to ROADMAP.md by humans. Include reproduction details so
        the claim is testable.
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: What did you expect?
    validations:
      required: true
  - type: textarea
    id: repro
    attributes:
      label: Steps to reproduce / command / battle seed
    validations:
      required: false

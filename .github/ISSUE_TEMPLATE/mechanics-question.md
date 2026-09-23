---
name: Mechanics research question
about: Ask about a Medarot 2 Core battle mechanic (drives research + devlog topics)
title: "[mechanics] "
labels: ["research"]
body:
  - type: markdown
    attributes:
      value: |
        Mechanics questions feed the Phase 0 research specs (docs/mechanics/)
        and often become devlog posts. The agent answers from the source
        index (docs/research/sources.md) with claim classification per
        docs/planning/content-rules.md — facts vs inference vs unknown.
  - type: textarea
    id: question
    attributes:
      label: What do you want to know?
      description: e.g. "How does Part Defense route damage?" or "What exactly does Propulsion affect?"
    validations:
      required: true
  - type: textarea
    id: context
    attributes:
      label: Where did you encounter it?
      description: In-game observation, guide, wiki page, etc. (optional)
    validations:
      required: false

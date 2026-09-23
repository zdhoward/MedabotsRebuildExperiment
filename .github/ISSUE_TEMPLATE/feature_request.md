---
name: Feature request
about: Suggest a feature, mechanic, or improvement for the agent to work on
title: "[feature] "
labels: ["feature-request"]
body:
  - type: markdown
    attributes:
      value: |
        Feature requests guide the human-maintained ROADMAP. The agent never
        implements directly from issues; humans promote accepted items into
        ROADMAP.md via PR. Research-backed suggestions (with sources) get
        priority.
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: What should exist or change, and why?
    validations:
      required: true
  - type: textarea
    id: evidence
    attributes:
      label: Evidence / sources
      description: Links, citations, or in-game observations supporting this (optional but strongly preferred)
    validations:
      required: false
  - type: dropdown
    id: area
    attributes:
      label: Area
      options:
        - Engine (battle mechanics)
        - Research / specs
        - Data (parts, medals, medabots)
        - Blog / site
        - Automation / CI
        - Other
    validations:
      required: true
  - type: textarea
    id: acceptance
    attributes:
      label: Suggested acceptance criteria
      description: How would we know it's done? (test-checkable if possible)
    validations:
      required: false

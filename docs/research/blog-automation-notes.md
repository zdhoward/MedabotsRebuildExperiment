# Blog Automation Research Notes

> Session research notes on automating the devlog blog. Follows
> `docs/planning/content-rules.md` (claim classification + confidence). Researched
> 2026-09-23. Scope: what architecture fits an Astro-on-Cloudflare-Pages repo with an
> AI agent committing posts via git — NOT hosted-WordPress pipelines.

## What we actually need vs what the market sells

**[DOCUMENTED / HIGH]** The mainstream "AI blog automation" tutorials all describe the
same pipeline: a content-ideas database (Google Sheet) triggers an automation hub
(Make.com / Activepieces / n8n), which calls an LLM API for title + body, then posts a
DRAFT to WordPress via REST API, then notifies a human for review
[Activepieces guide](https://www.activepieces.com/blog/automate-blog-writing-with-ai-a-step-by-step-guide-using-openai),
[eesel writeup](https://www.eesel.ai/blog/how-i-built-a-fully-automated-blog-using-ai).

**[INFERRED / HIGH]** None of those tool stacks apply to us directly, because our
publishing primitive is different: our "CMS" is a git branch + Astro content collection,
and our "draft-for-review" step is a GitHub pull request. The useful transferable idea
is the **pipeline shape**, not the tools:

```
idea source → AI generation → DRAFT state (not live) → human/CI review gate → publish
```

We already have this shape: STATE.json/ROADMAP.md (idea source) → agent session (AI
generation) → session branch + draft PR (draft state) → CI publish gate + human review
(review gate) → merge → Cloudflare Pages builds (publish).

**[DOCUMENTED / MEDIUM]** The eesel writeup's main criticism of DIY pipelines is that
raw LLM output is "text, not assets": no images, no structure, no internal links, and a
generic tone that fails E-E-A-T. Their remedy is a paid platform; our remedy is already
different and arguably stronger — the agent must cite real session artifacts
(`temp/session_report.json`, test output) and CI validates claimed metrics before
publish (`scripts/validate_post.py` per PROMPT.md, AGENTS.md rule 7).

**[DOCUMENTED / LOW]** AUTO-blogger
([github.com/AryanVBW/AUTO-blogger](https://github.com/AryanVBW/AUTO-blogger)) is a
WordPress-focused Python tool (Gemini rewriting + DALL-E images + WP REST API). Not
directly reusable; its relevant example is the self-updating GitHub-Actions-driven
automation pattern. The remaining links (sedestral, automatorplugin, spartner) are
WordPress/plugin-platform marketing pages — Tier 4/5 per content-rules.md; noted for
completeness, not used as evidence.

**[UNKNOWN]** The Medium post ("How I built a fully automated blog using GPT") is
Cloudflare-blocked from this environment and could not be read. No claims drawn from
it.

## Decisions for this repo (adopted this session)

1. **Astro blog scaffolded in `blog/`** with a content collection schema that REQUIRES
   the PROMPT.md frontmatter fields. The schema is the machine-enforced contract; the
   agent cannot publish a post that omits `commit_sha` or `metrics`.
2. **CI builds the site** on every PR. A post that fails the schema or the build never
   reaches Cloudflare. This is the "CI as publish gate" from `blog/README.md`, now real.
3. **Draft status vocabulary**: `status: draft` for WIP posts; session posts use
   `pass|fail` per PROMPT.md. The Astro schema validates the enum.
4. **Scheduling + issue-driven todo guidance** (GitHub issue templates for feature
   requests / roadmap suggestions, and validating `daily_agent.yml`) are staged NEXT —
   the blogging substrate must exist before the scheduler has something to publish.

## Open questions (next iteration)

- Exact `daily_agent.yml` CLI invocation still a placeholder — must be validated
  against the real agent CLI before enabling cron (already flagged in the handoff).
- Should `validate_post.py` also parse the built `dist/` to assert every post rendered?
- RSS via `@astrojs/rss` — wire at scaffold time (decision: yes, per blog/README.md).

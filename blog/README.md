# Blog — Astro on Cloudflare Pages

## Rules that govern content

- **`docs/planning/content-rules.md`** — the AI Researcher + Blogger ruleset
  (research integrity, claim classification, evidence tiers, no-hallucination,
  fact-check passes). Mandatory for every post.
- **`PROMPT.md`** (repo root) — article-specific requirements: frontmatter, archetype
  rotation, artifact citation. Single source of truth for article format.
- **`AGENTS.md`** (repo root) — the agent contract (one task per session, honest
  devlogs, failure protocol).

## Conventions

- Posts: `src/content/blog/YYYY-MM-DD-<slug>.md` with frontmatter per PROMPT.md
  (title, pubDate, task_id, archetype, status, featured_image, metrics, commit_sha).
  The content collection schema in `src/content.config.ts` REQUIRES these fields and
  validates types/enums — a post that omits them fails the build.
- Images live beside posts: `src/assets/YYYY-MM-DD/`.
- `public/ads.txt` is added only when AdSense is activated.
- RSS feed at `/rss.xml` via `@astrojs/rss`.

## Build & deploy

- Local: `npm install && npm run build` (or `npm run dev`).
- CI builds the site on every PR; a red build blocks publish.
- Cloudflare Pages, Git integration, build command `npm run build`, output `dist`,
  deploy only on green CI (Cloudflare build is the publish gate).

## Status vocabulary

- `draft` — WIP, not a session outcome.
- `pass` | `fail` — session outcome per PROMPT.md (validated against
  `temp/session_report.json`).

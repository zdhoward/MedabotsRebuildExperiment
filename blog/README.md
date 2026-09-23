# Blog — Astro on Cloudflare Pages

Scaffold (one-time, local):
```
npm create astro@latest blog -- --template blog --typescript --no-git
npx astro add rss   # or implement feed via @astrojs/rss
```

## Conventions
- Posts: `src/content/blog/YYYY-MM-DD-<slug>.md` with frontmatter per PROMPT.md
  (title, pubDate, task_id, archetype, status, featured_image, metrics, commit_sha).
- Images live beside posts: `src/assets/YYYY-MM-DD/`.
- Content collection schema MUST require the frontmatter fields above (validate in CI).
- `public/ads.txt` added only when AdSense is activated.

## Deploy
Cloudflare Pages, Git integration, build command `npm run build`, output `dist`,
deploy only on green CI (advanced: Cloudflare build is the publish gate).

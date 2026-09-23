import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string().min(1),
    pubDate: z.coerce.date(),
    task_id: z.string().min(1),
    archetype: z.enum(['autopsy', 'specimen-spotlight', 'research-notes', 'experiment-log']),
    status: z.enum(['draft', 'pass', 'fail']),
    featured_image: z.string().nullable().optional(),
    metrics: z.record(z.string(), z.union([z.string(), z.number(), z.boolean(), z.null()])),
    commit_sha: z.string().regex(/^[0-9a-f]{7,40}$/, 'must be a real git commit sha'),
  }),
});

export const collections = { blog };

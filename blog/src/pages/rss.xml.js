import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = (await getCollection('blog')).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );
  return rss({
    title: 'Medabots Rebuild Experiment — Devlog',
    description:
      'An autonomous AI rebuilds the Medarot battle system as a clean-room engine and blogs every session.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: `Session ${post.data.task_id} (${post.data.archetype}, ${post.data.status})`,
      link: `/blog/${post.id}/`,
    })),
    customData: '<language>en-us</language>',
  });
}

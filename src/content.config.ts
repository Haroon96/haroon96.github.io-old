import { defineCollection, z } from 'astro:content';

import { file } from 'astro/loaders';

const publications = defineCollection({
    loader: file("src/data/publications.json"),
    schema: z.object({
        title: z.string(),
        authors: z.array(z.string()),
        year: z.number(),
        venue: z.string(),
        urls: z.array(z.object({
            name: z.string(),
            url: z.string()
        }))
    })
});

const news = defineCollection({
    loader: file("src/data/news.json"),
    schema: z.object({
        text: z.string(),
        month: z.string(),
        year: z.number(),
    })
});

const talks = defineCollection({
    loader: file("src/data/talks.json"),
    schema: z.object({
        title: z.string(),
        year: z.number(),
        venue: z.string(),
        urls: z.array(z.object({
            name: z.string(),
            url: z.string()
        }))
    })
});

const podcasts = defineCollection({
    loader: file("src/data/podcasts.json"),
    schema: z.object({
        title: z.string(),
        year: z.number(),
        host: z.string(),
        urls: z.array(z.object({
            name: z.string(),
            url: z.string()
        }))
    })
});

const photos = defineCollection({
    loader: file('src/data/photos.json'),
    schema: z.object({
        photo: z.string(),
        description: z.string()
    })
});

const misc = defineCollection({
    loader: file('src/data/misc.json'),
    schema: z.object({
        photo: z.string(),
        description: z.string()
    })
});

export const collections = { publications, news, talks, podcasts, photos, misc };
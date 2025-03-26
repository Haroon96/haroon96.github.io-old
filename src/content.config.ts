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

export const collections = { publications };
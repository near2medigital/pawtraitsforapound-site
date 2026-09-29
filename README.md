# Pawtraits for a Pound

Static production website for https://pawtraitsforapound.co.uk.

## Stack

- Static HTML/CSS
- Cloudflare Pages hosting
- Tally order-form embed
- Make + SumUp fulfilment stack

## Deployment

Production branch: `main`.

Cloudflare Pages deploys the repository root with no build command.

## Blog

The public blog lives at `/blog/` and uses the same static HTML/CSS architecture as the main site.

Publishing rules are documented in `BLOG-PUBLISHING.md`. Article pages should live at `/blog/<slug>/index.html`, update the blog index, then deploy through the normal GitHub -> Cloudflare Pages workflow.

The blog index is indexable. GitHub Actions automatically rebuilds `sitemap.xml` from indexable canonical pages before each Cloudflare deployment, so new article pages are added without a manual sitemap edit.
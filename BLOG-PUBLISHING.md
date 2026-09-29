# Pawtraits Blog Publishing Procedure

The public blog lives at `https://pawtraitsforapound.co.uk/blog/`.

## Architecture

- Homepage remains the commercial one-page experience at `/`.
- Blog index lives at `/blog/`.
- Every article gets a descriptive slug: `/blog/example-article/`.
- Each article is static HTML and shares `/styles.css`.
- No CMS, database or separate blog host is required.
- Publishing is Git commit -> push to `main` -> GitHub Actions -> Cloudflare Pages.

## Article requirements

Every published article must include:

1. Unique title and meta description.
2. Canonical URL on `pawtraitsforapound.co.uk`.
3. Open Graph title, description, URL and image.
4. `BlogPosting` structured data with headline, description, datePublished, dateModified, author/publisher and canonical URL.
5. Breadcrumb links: Home -> Blog -> Article.
6. A visible published/updated date.
7. At least one contextually useful link back to the commercial Pawtraits offer where relevant.
8. Navigation and footer matching the rest of the site.
9. Google Analytics Consent Mode implementation matching the current site.
10. No em dashes.

## Publishing sequence

1. Draft and fact-check the article.
2. Choose final slug, title, description, category and social image.
3. Create `blog/<slug>/index.html`.
4. Add the article card to `blog/index.html`.
5. Validate canonical, metadata, schema, internal links and no-em-dash rule.
6. Commit and push. GitHub Actions rebuilds `sitemap.xml` automatically from indexable canonical pages before deployment.
7. Verify the GitHub Actions deployment, live article URL and live sitemap.

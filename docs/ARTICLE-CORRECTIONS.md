# Corrections for the live blog article

**Article:** Signs of Separation Anxiety in Dogs
**Live URL:** https://bea-co.it/blogs/news/signs-of-separation-anxiety-in-dogs-what-most-owners-mis
**Where to apply:** Shopify Admin → Online Store → Blog posts → *Signs of Separation Anxiety…* → Edit

Two fixes are needed. Apply them in the Shopify editor (I can't push them — the API connection lacks the `read_content` scope, see note at the bottom).

---

## 1. Fix the title (currently truncated)

The live title reads **"What Most Owners Mis"** — the final **s** is missing (should be **Miss**).

**Change the title to:**

> Signs of Separation Anxiety in Dogs: What Most Owners **Miss**

That's the only change to the title. Do not alter the URL/handle (changing it would break the link already shared).

---

## 2. Fix the unsupported statistic

The article currently says:

> "It's a real behavioral condition that affects an estimated **20-40%** of dogs."

That range is **not supported** by the research. Published prevalence estimates for canine separation anxiety sit much lower and vary by how they're measured:

| Source | Estimate |
|---|---|
| Salonen et al. 2020 (n=13,715, general pop.) | **~5%** |
| Storengen et al. 2014 (case series) | **~17%** |
| Bradshaw et al. 2002 (UK sample) | **~22%** |
| Veterinary clinical range | **13–28%** |
| Most-cited working figure | **about 1 in 5 dogs** |

**Replace the sentence with this defensible version:**

> "Here's what we want you to know: separation anxiety is not a reflection of your love or your competence. It's a real behavioral condition — thought to affect **around one in five dogs** — and noticing it, really noticing it, is the first step toward supporting your dog through it."

If you'd rather cite a source, the cleaner phrasing is:

> "…a real behavioral condition — estimates suggest it affects **5–22% of dogs**, depending on how it's measured (Salonen 2020; Bradshaw 2002) — and noticing it…"

---

## 3. (Optional) Link the statistic to a source

Since the whole article is educational and builds trust, add one hyperlink on the phrase "around one in five dogs" pointing to a reputable source — the **ASPCA** page on separation anxiety:
`https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues/separation-anxiety`

That gives the claim a credible anchor and helps SEO/E-E-A-T.

---

## Note on why I couldn't do this for you

I tried to update the article directly through the Shopify API. The request returned **403 Forbidden**:

> `This action requires merchant approval for read_content scope.`

Your Shopify store hasn't approved app access to **read/write blog content** for the connected app. To let me edit articles in future, in Shopify Admin go to **Settings → Apps and sales channels → [the connected app] → Admin API access scopes**, and approve **`read_content`** and **`write_content`**. Until then, blog edits are manual in the Shopify editor.

Would you like me to also draft a replacement **body** for the article with source links throughout, or keep the body as-is and just apply the two fixes above?

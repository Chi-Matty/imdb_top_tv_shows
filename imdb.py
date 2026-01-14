from playwright.async_api import async_playwright
import asyncio
import re
import random


async def imdb_tv():
    url = "https://m.imdb.com/chart/toptv/"
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--no-sandbox"]
        )

        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/128.0.0.0 Safari/537.36"
            )
        )

        page = await context.new_page()
        await page.goto(url, wait_until="domcontentloaded")

        links = await page.eval_on_selector_all(
            "a[href*='/title/tt']",
            "els => els.map(el => el.href)"
        )

        normalized_links = []
        for link in links:
            match = re.search(r"(https://m\.imdb\.com/title/tt\d+)", link)
            if match:
                normalized_links.append(match.group(1))

        links = list(dict.fromkeys(normalized_links))

        for idx, link in enumerate(links[:60], start=1):
            try:
                await page.goto(link, timeout=60000)
            except:
                print(f"Failed to load page {link}")
                continue

            try:
                title = await page.inner_text(
                    "h1[data-testid='hero__pageTitle'] span.hero__primary-text"
                )
            except:
                title = None

            try:
                rating = await page.inner_text(
                    "div[data-testid='hero-rating-bar__aggregate-rating__score'] span"
                )
            except:
                rating = None

            try:
                creator = await page.eval_on_selector(
                    "a.ipc-metadata-list-item__list-content-item--link",
                    "el => el.innerText"
                )
            except:
                creator = None

            try:
                reviews = await page.inner_text("a.isReview span.score")
            except:
                reviews = None

            results.append({
                "Rank": idx,
                "Title": title,
                "Rating": rating,
                "Creator": creator,
                "Reviews": reviews
            })

            await asyncio.sleep(random.uniform(0.3, 0.8))

        await browser.close()

    return results


async def main():
    data = await imdb_tv()
    print("Scrape Completed!")
    print(data)


asyncio.run(main())


import pandas as pd
df = pd.DataFrame(data)

df.to_csv("IMDb Top Tv Shows", index=False)

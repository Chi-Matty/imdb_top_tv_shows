# IMDb Top 250 TV Series Data Scraper (Playwright)

Automated scraping of 250 TV shows, collected title, rating, creators, and reviews using Playwright and Python.

## Technologies Used
    • Python • Playwright • Asyncio • Pandas

![WhatsApp Image 2026-01-14 at 2 12 02 AM](https://github.com/user-attachments/assets/bbdf586a-b89d-4429-b092-f7ca582a9cb9)


## Project Summary
Designed an asynchronous web scraping pipeline with Playwright, asyncio, and Pandas to extract web data from IMDb's Top 250 TV series. The pipeline automated navigation of JavaScript-rendered pages, normalized show URLs with regex, and applied resilient error handling for failed requests—achieving reliable data extraction. This initiative produced a clean CSV dataset ready for analytics, visualization, or integration into media recommendation systems.

### The workflow:
* Asynchronous orchestration with asyncio to scale requests and minimize runtime.
* Dynamic rendering handling via Playwright to reliably scrape JavaScript-heavy pages.
* Normalized extracted show links using regex for consistency and deduplication.
* Error resilience with retry logic to handle failed page loads gracefully.
* Data structuring with Pandas, exporting results into a clean, analysis-ready CSV.

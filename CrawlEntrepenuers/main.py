from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.cityu.edu.hk"
START_URL = f"{BASE_URL}/hktech300/start-ups/all-start-ups?page="
PAGE_RANGE = range(1, 41)
OUTPUT_FOLDER = Path(r"C:\Users\User\Projects\AssignmentAscend")
TIMEOUT = 60000
WAIT_TIME = 3000


def parse_company_cards(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for card in soup.select("div.card.fund.team"):
        link = card.find("a", href=True)
        if not link:
            continue

        name = link.get_text(strip=True)
        if not name:
            continue

        results.append(
            {
                "Company Name": name,
                "CityU URL": urljoin(BASE_URL, link["href"]),
                "Email": "No Info Found",
                "Company Website": "No Info Found",
            }
        )

    return results


def extract_company_details(page, result):
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    email_link = soup.find("a", href=lambda href: href and href.startswith("mailto:"))
    if email_link:
        result["Email"] = email_link["href"].replace("mailto:", "").strip()

    company_heading = soup.find("h2", string=lambda text: text and "Company website" in text)
    if company_heading:
        website_link = company_heading.find_next_sibling("a")
        if website_link and website_link.get("href"):
            result["Company Website"] = website_link.get("href").strip()


def save_csv(results, output_path):
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")


def merge_csv_files(output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)
    csv_files = sorted(output_folder.glob("cityu_startups_*.csv"))
    if not csv_files:
        print("No page CSV files found to merge.")
        return

    merged_df = pd.concat([pd.read_csv(path) for path in csv_files], ignore_index=True)
    merged_df.to_csv(output_folder / "cityu_startups_merged_output.csv", index=False, encoding="utf-8-sig")
    print(f"Merged {len(csv_files)} files into cityu_startups_merged_output.csv")


def scrape_page(page, page_num):
    page.goto(f"{START_URL}{page_num}", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)

    results = parse_company_cards(page.content())
    cards = page.locator("div.card.fund.team")
    count = cards.count()
    print(f"Page {page_num}: found {count} cards")

    for index in range(min(count, len(results))):
        card = cards.nth(index)
        card.click()
        page.wait_for_timeout(WAIT_TIME)
        extract_company_details(page, results[index])
        page.go_back()
        page.wait_for_timeout(500)

    return results


def main():
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, slow_mo=500)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()
        page.set_default_timeout(TIMEOUT)

        all_results = []
        for page_num in PAGE_RANGE:
            try:
                results = scrape_page(page, page_num)
                if results:
                    page_csv = OUTPUT_FOLDER / f"cityu_startups_{page_num:02d}.csv"
                    save_csv(results, page_csv)
                    print(f"Saved page {page_num} results to {page_csv}")
                    all_results.extend(results)
            except Exception as exc:
                print(f"Error scraping page {page_num}: {exc}")

        if all_results:
            save_csv(all_results, OUTPUT_FOLDER / "cityu_startups_all_pages.csv")
            merge_csv_files(OUTPUT_FOLDER)


if __name__ == "__main__":
    main()

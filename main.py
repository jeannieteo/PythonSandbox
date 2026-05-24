import os
import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

#url = "https://www.cityu.edu.hk/hktech300/start-ups/all-start-ups?page=1"
url = "https://www.cityu.edu.hk/hktech300/start-ups/all-start-ups?page="
base_url = "https://www.cityu.edu.hk"
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        slow_mo=500
    )
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        )
    )
    page = context.new_page()
    page.set_default_timeout(60000)
    for page_num in range(40, 41): # Loop through pages 1 to 40
        page.goto(url + str(page_num), wait_until="domcontentloaded")
        #page.wait_for_timeout(8000) # Give anti-bot scripts time to run and load content
    
        html = page.content() # Get the page content after waiting for it to load

        soup = BeautifulSoup(html, "html.parser")
        all_div = soup.find_all('div', class_='card fund team') # find all div with class name 'card fund team' on the page
        results = []
        for div in all_div:
            # find all <a> tags in this div
            a_tags = div.find_all("a")
            for a in a_tags:
                text = a.get_text(strip=True)
                # ignore image-only <a>
                if text:
                    href = a.get("href")
                    full_url = urljoin(base_url, href)
                    results.append({
                    "Company Name": text,
                    "CityU URL": full_url
                })

        # add this for email and website extraction
        cards = page.locator("div.card") # get all 18 div with class name 'card fund team' on the page
        count = cards.count()
        print("Total cards:", count)
        for i in range(count): # For all 18 cards, click each one to go to the individual page 
            card = cards.nth(i)
            card.click()
            page.wait_for_timeout(3000)  # wait for 3 seconds
            html_individual = page.content()
            soup_individual = BeautifulSoup(html_individual, "html.parser")
            # find the email
            soup_email = soup_individual.find("a", href=lambda href: href and "mailto:" in href)
            if soup_email:  
                email = soup_email.get("href").replace("mailto:", "")
                print(f"Email found: {email}")
                results[i]["Email"] = email
            else:
                print("No Info Found")
                results[i]["Email"] = "No Info Found"
            # find the company website URL using the H2 tag as a reference point
            soup_company = soup_individual.find("h2", string=" Company website")
            if soup_company:
                company_url = soup_company.find_next_sibling("a")
                if company_url:
                    results[i]["Company Website"] = company_url.get("href")
                else:
                    results[i]["Company Website"] = "No Info Found"
            else:
                results[i]["Company Website"] = "No Info Found"
            page.go_back()

        # convert to dataframe for each page I don't like to lose data if the script crashes in the middle, so I save a csv for each page as well
        df = pd.DataFrame(results)
        print(df.head())
        # export csv
        df.to_csv("cityu_startups" + str(page_num) + ".csv", index=False, encoding="utf-8-sig")
        print("CSV saved successfully")
    # convert to dataframe at the very end to save all data together in one file
    folder_path = r'C:\Users\User\Projects\AssignmentAscend'
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    df = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in files], ignore_index=True)
    df.to_csv('cityu_startups_merged_output.csv', index=False)
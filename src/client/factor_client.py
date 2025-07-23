import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

import os
import logging

load_dotenv()

logger = logging.getLogger(__name__)


LOGIN_URL = "https://myaccount.redpathbruce.co.uk/"
USERNAME = os.getenv('REDPATHBRUCE_USERNAME')
PASSWORD = os.getenv('REDPATHBRUCE_PASSWORD')


async def check_balance():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(LOGIN_URL)

        try:
            # Fill in login form (update selectors as needed)
            await page.fill('input[name="UserName"]', USERNAME)
            await page.fill('input[name="Password"]', PASSWORD)
            await page.click('input#submit')
            # Wait for navigation or content to load
            await page.wait_for_load_state('networkidle')

            # Extract page content
            content = await page.content()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            balance_tag = soup.find('p', class_='balanceabsolute')
            if balance_tag:
                balance_text = balance_tag.get_text(strip=True)
                if 'Current Balance:' in balance_text:
                    amount = balance_text.split('Current Balance:')[-1].strip()
                    if amount != '£0.00':
                        return f"Amount pending: {amount}"
                    else:
                        return "No pending balance"
                else:
                    raise ValueError("Balance field not found.")
            else:
                raise ValueError("Balance tag not found.")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(check_balance())

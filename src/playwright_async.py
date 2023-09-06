"""Async playwright"""
import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()

        page = await browser.new_page()
        await page.goto('http://playwright.dev')
        print(await page.title())


asyncio.run(main())

"""Async playwright"""
import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)

        page = await browser.new_page()
        await page.goto('http://playwright.dev')
        await page.screenshot(path="example.png")


asyncio.run(main())

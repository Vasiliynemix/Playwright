"""Sync playwright"""
from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    page = browser.new_page()
    page.goto('http://playwright.dev')
    print(page.title())

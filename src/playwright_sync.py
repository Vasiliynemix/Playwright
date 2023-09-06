"""Sync playwright"""
import time

from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=50)

    page = browser.new_page()
    page.goto('http://playwright.dev')
    page.screenshot(path="example.png")

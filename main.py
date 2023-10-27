# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
import time

from playwright.async_api import Page, expect
from playwright.sync_api import sync_playwright


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()
    page.goto("https://trello.com/pt-BR")
    page.locator('xpath=/html/body/div[1]/header[1]/div/div[1]/div[2]/a[1]').click()
    time.sleep(5)
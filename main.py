# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
import time

from playwright.async_api import Page, expect
from playwright.sync_api import sync_playwright
from login import *

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()
    page.goto("https://trello.com/pt-BR")
    page.locator('xpath=/html/body/div[1]/header[1]/div/div[1]/div[2]/a[1]').click()
    page.locator('xpath=//*[@id="username"]').fill(email)
    page.locator('xpath=//*[@id="login-submit"]').click()
    page.locator('xpath=//*[@id="password"]').fill(senha)
    page.locator('xpath=//*[@id="login-submit"]').click()
    time.sleep(5)
    page.goto("https://trello.com/b/sveze0kI/t%C3%B3picos")
    page.locator('xpath=/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div[1]/div[3]/div[2]/ol/li/div/div[2]/button[1]').click()
    page.locator('xpath=/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div[1]/div[3]/div[2]/ol/li/div/ol/form/textarea').fill('teste')
    page.locator('xpath=/html/body/div[1]/div[2]/div[1]/div/div/div/nav/div[1]/div/div[4]').click()
    time.sleep(3)
    page.locator('xpath=/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div[1]/div[3]/div[2]/ol/li/div/ol/li/div/div/a').click()
    page.locator('xpath=/html/body/div[1]/div[2]/div[3]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/p').fill('teste')
    page.locator('xpath=/html/body/div[1]/div[2]/div[3]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/button[1]').click()
    time.sleep(7)
    page.locator('xpath=/html/body/div[1]/div[2]/div[3]/div/div/a').click()
    time.sleep(5)
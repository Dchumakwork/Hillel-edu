import pytest
from playwright.sync_api import sync_playwright
from homework_28to30 import QautoSource

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def qauto_source(browser):
    context = browser.new_context(http_credentials={"username": "guest", "password": "welcome2qauto"})
    page = context.new_page()
    page.goto('https://qauto2.forstudy.space/')
    return QautoSource(page)


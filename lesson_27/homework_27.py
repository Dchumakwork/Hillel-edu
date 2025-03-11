import pytest
from playwright.sync_api import sync_playwright

url = 'https://tracking.novaposhta.ua/#/uk'
ttn_number = '20 4511 0961 1421'
input_selector = '#en'
find_btn_selector = '#np-number-input-desktop-btn-search-en'
status_selector = '#chat > header > div.header__parcel-dynamic-status.px-4.d-flex.align-center > div.flex-grow-1 > div.header__status-text'

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_nova_poshta_tracking(page):
    print(f'\nGoing to {url}...')
    page.goto(url)
    print('Entering the TTN number...')
    page.fill(input_selector, ttn_number)
    print('Clicking the "find" button...')
    page.click(find_btn_selector)
    print('Waiting for TTN status')
    page.wait_for_selector(status_selector)
    status = page.inner_text(status_selector)
    assert status.strip() == "Отримана", 'Unexpected status'
    page.wait_for_timeout(3000)
    print(f"Status is: {status}")
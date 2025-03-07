from playwright.sync_api import sync_playwright

url_to_test = 'https://qauto2.forstudy.space/'

logo_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > a'
home_elem_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > a'
about_btn_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(2)'
contacts_btn_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(3)'
signin_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.btn.btn-outline-white.header_signin'
guest_login_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.header-link.-guest'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(http_credentials={"username": "guest", "password": "welcome2qauto"})
    page = context.new_page()

    page.goto(url_to_test)
    page.wait_for_timeout(3000)

    # header elements visibility checking
    selectors_list = [['logo', logo_selector], ['home', home_elem_selector], ['about', about_btn_selector], ['contacts', contacts_btn_selector], ['signin', signin_selector], ['login', guest_login_selector]]
    elements_are_visible = True
    print('Checking header elements...')
    for elem in selectors_list:
        try:
            assert page.locator(elem[1]).is_visible(), f'{elem[0]} is missed'
        except AssertionError as e:
            elements_are_visible = False
            print(e)
    if elements_are_visible:
        print('All elements are visible')
    page.wait_for_timeout(2000)

    # guest loging check
    is_logged_in = False
    profile_selector = '#userNavDropdown'
    try:
        print('\nTrying to log in...')
        page.click(guest_login_selector, timeout=3000)
        curr_url = page.url
        page.wait_for_timeout(2000)
        assert curr_url == url_to_test + 'panel/garage', 'URL is wrong'
        assert page.locator(profile_selector).is_visible(), 'Profile is not faund'
        is_logged_in = True
        print('Successful authorization')
        page.wait_for_timeout(2000)
    except AssertionError as e:
        print(f"Athorization failed: {e}")
        page.wait_for_timeout(2000)

    if is_logged_in:
        try:
            print('\nLogging out...')
            page.click(profile_selector)
            page.wait_for_timeout(2000)
            prof_log_out_selector = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > app-user-nav > div > nav > button'
            page.wait_for_selector(prof_log_out_selector, timeout=3000)
            page.click(prof_log_out_selector)
            curr_url = page.url
            page.wait_for_timeout(2000)
            assert curr_url == url_to_test, 'URL is wrong'
            assert page.locator(guest_login_selector).is_visible(), 'Login button is unavailable'
            is_logged_in = False
            print('Come back soon')
            page.wait_for_timeout(2000)
        except AssertionError as e:
            print(f'Something went wrong: {e}')
            page.wait_for_timeout(2000)
from homework_28 import generate_random_number

def test_user_registration(qauto_source):
    qauto_source.open_registration_form()
    qauto_source.fill_registration_form(
        name="Dimon",
        lastname="Hillelov",
        # do not forget to change the email for each attempt
        email=f"test{generate_random_number()}user{generate_random_number()}@te.st",
        password="Password123",
        repeat_password="Password123"
    )

    assert qauto_source.page.url == qauto_source.loggedin_page
    assert qauto_source.page.locator(qauto_source.profile_menu).is_visible()

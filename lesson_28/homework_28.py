from playwright.sync_api import Page
import random
def generate_random_number():
    return random.randint(1, 1000)


class QautoSource:
    def __init__(self, page: Page):
        self.page = page
        self.signin_btn = ('body > app-root > app-global-layout > div > div > app-header > header > div > div > '
                           'div.header_right.d-flex.align-items-center > button.btn.btn-outline-white.header_signin')
        self.goto_reg_btn = ('body > ngb-modal-window > div > div > app-signin-modal > '
                             'div.modal-footer.d-flex.justify-content-between > button.btn.btn-link')
        self.name_input = '#signupName'
        self.lastname_input = '#signupLastName'
        self.reg_email_input = '#signupEmail'
        self.reg_password_input = '#signupPassword'
        self.repeat_password_input = '#signupRepeatPassword'
        self.registration_btn = 'body > ngb-modal-window > div > div > app-signup-modal > div.modal-footer > button'
        self.loggedin_page = 'https://qauto2.forstudy.space/panel/garage'
        self.profile_menu = '#userNavDropdown'

    def fill_registration_form(self, name, lastname, email, password, repeat_password):
        self.page.fill(self.name_input, name)
        self.page.fill(self.lastname_input, lastname)
        self.page.fill(self.reg_email_input, email)
        self.page.fill(self.reg_password_input, password)
        self.page.fill(self.repeat_password_input, repeat_password)
        self.page.wait_for_timeout(2000)
        self.page.click(self.registration_btn)
        self.page.wait_for_load_state('load')
        self.page.wait_for_timeout(3000)

    def open_registration_form(self):
        self.page.click(self.signin_btn)
        self.page.click(self.goto_reg_btn)
        self.page.wait_for_load_state('load')
        self.page.wait_for_timeout(1000)


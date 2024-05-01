import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from helpers.common_steps import clear_data_and_run_app
from helpers.config_importer import ConfigImporter
from helpers.error_message import error_message
from helpers.config_env import config_env
from pytest_testrail.plugin import pytestrail

class TestLogin:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        clear_data_and_run_app(self.driver)
        self.config_env = config_env()
        self.config_importer = ConfigImporter()
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.error = error_message()
        self.login = self.config_env['login']
        self.password = self.config_env['password']

    # Mark test as a "login_negative" to run marked tests in the future
    @pytestrail.case('C853')
    @pytest.mark.login_negative
    def test_login_empty_input(self, driver):
        # Initialization
        self.init(driver)

        # The User click on Login button
        self.register_page.click_login_button()

        # The User clear username field empty
        self.login_page.enter_username('')

        # The User clear password field empty
        self.login_page.enter_password('')

        # The User keep input fields blank and click on Login button
        self.login_page.click_login_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])

        # The User see 'user password is empty' error message
        #assert self.login_page.error_message_is_visible(self.error['login_password_empty'])

    # Mark test as a "login_negative" to run marked tests in the future
    @pytestrail.case('C851')
    @pytest.mark.login_negative
    def test_login_username_incorrect(self, driver):
        # Initialization
        self.init(driver)

        # The User click on Login button
        self.register_page.click_login_button()

        # The User enter invalid username
        self.login_page.enter_username(self.config_importer.config_username_incorrect())

        # The User enter password
        self.login_page.enter_password(self.password)

        # The User click on Login button
        self.login_page.click_login_button()

        # The User see 'username or password is invalid' error message
        assert self.login_page.error_message_is_visible(self.error['username_incorrect'])

    # Mark test as a "login_negative" to run marked tests in the future
    @pytestrail.case('C852')
    @pytest.mark.login_negative
    def test_login_password_short(self, driver):
        # Initialization
        self.init(driver)

        # The User click on Login button
        self.register_page.click_login_button()

        # The User enter username
        self.login_page.enter_username(self.login)

        # The User enter invalid password
        self.login_page.enter_password(self.config_importer.config_user_password_short())

        # The User click on Login button
        self.login_page.click_login_button()

        # The User see 'username or password is invalid' error message
        assert self.login_page.error_message_is_visible(self.error['short_password'])

    # Mark test as a "login" to run marked tests in the future
    #@pytestrail.case('C832')
    @pytest.mark.login_positive
    def test_login(self, driver):
        # Initialization
        self.init(driver)
        # # # # # # # # # Initialization # # # # # # # # # # # # #

        # The User click on Login button
        self.register_page.click_login_button()

        # The User enter username
        self.login_page.enter_username(self.login)

        # The User enter password
        self.login_page.enter_password(self.password)

        # The User click on Login button
        self.login_page.click_login_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on Skip button
        self.login_page.click_skip_button()

        # The User click on Skip button
        self.login_page.click_skip_button()

        # The User click on Skip activation button
        self.login_page.click_skip_activation_button()

        # The user select device
        self.home_page.select_prosumer_device()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User see the bottom navigation bar
        assert self.home_page.bottom_navigation_bar_is_visible()

import time
import pytest
from api.api_validate_profile import validate_profile
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from helpers.common_steps import clear_data_and_run_app
from helpers.config_importer import ConfigImporter
from helpers.data_generator import GenerateUserData
from helpers.error_message import error_message
from helpers.success_message import success_message
from helpers.config_env import config_env


# Global variable
pytest.login = None
pytest.password = None


class TestRegister:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        clear_data_and_run_app(self.driver)
        self.config_env = config_env()
        self.config_importer = ConfigImporter()
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.env_path = self.config_importer.config_env()
        self.error = error_message()
        self.success = success_message()
        self.faker = GenerateUserData()
        self.login = self.config_env['login']

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_empty(self, driver):
        # Initialization
        self.init(driver)

        # The user click Register button
        self.register_page.click_register_button()

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_password_empty(self, driver):
        # Initialization
        self.init(driver)

        # The user click Register button
        self.register_page.click_register_button()

        # The user enter username
        self.register_page.enter_username(self.config_importer.config_username_invalid())

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_incorrect(self, driver):
        # Initialization
        self.init(driver)

        # The user click Register button
        self.register_page.click_register_button()

        # The user enter incorrect username
        self.register_page.enter_username(self.config_importer.config_username_incorrect())

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['username_incorrect'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_password_short(self, driver):
        # Initialization
        self.init(driver)

        # The user click Register button
        self.register_page.click_register_button()

        # The user enter username already exists
        self.register_page.enter_username(self.config_importer.config_username_invalid())

        # The user enter username already exists
        self.register_page.enter_password(self.config_importer.config_user_password_short())

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['short_password'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_exists(self, driver):
        # Initialization
        self.init(driver)

        # The user click Register button
        self.register_page.click_register_button()

        # The user enter username already exists
        self.register_page.enter_username(self.login)

        # The user enter password
        self.register_page.enter_password(self.config_importer.config_user_password_invalid())

        # The user click Register button
        self.register_page.click_register_button()
        time.sleep(2)

        # The User see 'username is empty' error message
        #assert self.register_page.pop_up_is_visible(self.error['user_exists_pop_up_title'])

    # Mark test as a "register_positive" to run marked tests in the future
    @pytest.mark.register_positive
    def test_register(self, driver):
        # Initialization
        self.init(driver)
        pytest.login = self.faker.email()
        pytest.password = self.faker.password()

        # The user click Register button
        self.register_page.click_register_button()

        # The user enter username
        self.register_page.enter_username(pytest.login)

        # The user enter password
        self.register_page.enter_password(pytest.password)

        # The user click Register button
        self.register_page.click_register_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User see 'username is empty' error message
        assert self.register_page.check_verify_email_title()

        # The User validate account
        validate_profile(pytest.login, pytest.password)

    # Mark test as a "register_login" to run marked tests in the future
    @pytest.mark.register_login
    def test_login(self, driver):
        # Initialization
        self.init(driver)

        # The User click on Login button
        self.register_page.click_login_button()

        # The User enter username
        self.login_page.enter_username(pytest.login)

        # The User enter password
        self.login_page.enter_password(pytest.password)

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

        # The User see the bottom navigation bar
        assert self.home_page.bottom_navigation_bar_is_visible()

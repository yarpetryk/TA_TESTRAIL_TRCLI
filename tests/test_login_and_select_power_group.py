from helpers.config_env import config_env
from helpers.common_steps import clear_data_and_run_app
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


def test_login(driver):
    # # # # # # # # # Initialization # # # # # # # # # # # # #
    clear_data_and_run_app(driver)
    config_environment = config_env()
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    login = config_environment['login']
    password = config_environment['password']
    # # # # # # # # # Initialization # # # # # # # # # # # # #

    # The User click on Login button
    register_page.click_login_button()

    # The User enter username
    login_page.enter_username(login)

    # The User enter password
    login_page.enter_password(password)

    # The User click on Login button
    login_page.click_login_button()

    # The user wait when spinner is finished
    home_page.wait_until_spinner_will_be_invisible()

    # The User click on Skip button
    login_page.click_skip_button()

    # The User click on Skip button
    login_page.click_skip_button()

    # The User click on Skip activation button
    login_page.click_skip_activation_button()

    # The user wait when spinner is finished
    home_page.wait_until_spinner_will_be_invisible()

    # The user select device
    home_page.select_power_group()

    # The User see the bottom navigation bar
    assert home_page.bottom_navigation_bar_is_visible()

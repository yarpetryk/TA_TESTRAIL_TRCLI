import allure
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators
from pages.base_pages import BasePage


class LoginPage(BasePage):
    """Description """
    @allure.step("And user enter correct email")
    def enter_username(self, text):
        #self.find_element_and_send_key(LoginPageLocators.USERNAME_FIELD, text)
        el = self.find_all_elements(LoginPageLocators.USERNAME_FIELD)[0]
        el.clear() and el.send_keys(text)


    @allure.step("And user enter correct password")
    def enter_password(self, text):
        #self.find_element_and_send_key(LoginPageLocators.PASSWORD_FIELD[1], text)
        el = self.find_all_elements(LoginPageLocators.USERNAME_FIELD)[1]
        el.clear() and el.send_keys(text)

    @allure.step("And user click login button")
    def click_login_button(self):
        self.find_all_elements(LoginPageLocators.LOGIN_BUTTON)[0].click()

    @allure.step("And user see input empty error message")
    def error_message_is_visible(self, error_message):
        self.is_element_enabled((By.XPATH, LoginPageLocators.ERROR_MESSAGE.format(name=error_message)))
        return True

    @allure.step("And user click skip button")
    def click_skip_button(self):
        self.find_element_and_click(LoginPageLocators.SKIP_BUTTON)

    @allure.step("And user click skip activation button")
    def click_skip_activation_button(self):
        self.find_element_and_click(LoginPageLocators.SKIP_ACTIVATION_BUTTON)

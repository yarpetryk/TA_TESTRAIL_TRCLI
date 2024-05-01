import allure
from pages.locators import RegisterPageLocators
from pages.base_pages import BasePage


class RegisterPage(BasePage):
    """Description """
    @allure.step("And user click register button")
    def click_register_button(self):
        self.find_element_and_click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("And user enter username")
    def enter_username(self, text):
        el = self.find_all_elements(RegisterPageLocators.INPUT_FIELD)[0]
        el.clear() and el.send_keys(text)

    @allure.step("And user enter password")
    def enter_password(self, text):
        el = self.find_all_elements(RegisterPageLocators.INPUT_FIELD)[1]
        el.clear() and el.send_keys(text)

    @allure.step("And user click login button")
    def click_login_button(self):
        self.find_element_and_click(RegisterPageLocators.LOGIN_BUTTON)

    @allure.step("And user <verify e-mail>")
    def check_verify_email_title(self):
        return self.find_element(RegisterPageLocators.USER_REGISTERED)

    @allure.step("And user <verify e-mail>")
    def check_error_pop_up(self):
        return self.find_element(RegisterPageLocators.USER_ALREADY_REGISTERED)


    @allure.step("And user see error pop up")
    def error_message_is_visible(self, error_message):
        el = self.find_element(RegisterPageLocators.ERROR_MESSAGE)
        if el.text == error_message:
            return True



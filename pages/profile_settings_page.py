import allure
from pages.locators import ProfileSettingsPageLocators
from pages.base_pages import BasePage


class ProfileSettingsPage(BasePage):
    """Description """
    @allure.step("And user click on the reset password item")
    def click_reset_password_item(self):
        self.find_element_and_click(ProfileSettingsPageLocators.RESET_PASSWORD_ITEM)

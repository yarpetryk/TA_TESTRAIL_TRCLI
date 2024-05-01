import allure
from pages.locators import ProfilePageLocators
from pages.base_pages import BasePage


class ProfilePage(BasePage):
    """Description """
    @allure.step("And user see log out menu item")
    def log_out_menu_item_is_visible(self):
        self.is_element_enabled(ProfilePageLocators.LOG_OUT_ITEM)
        return True

    @allure.step("And user click on the gear icon button")
    def click_gear_icon(self):
        self.find_element_and_click(ProfilePageLocators.GEAR_ICON)

    @allure.step("And user click on the house item")
    def click_house_item(self):
        self.find_element_and_click(ProfilePageLocators.HOUSE_ITEM)

    @allure.step("And user click on the device item")
    def click_device_item(self):
        self.find_element_and_click(ProfilePageLocators.DEVICE_ITEM)

    @allure.step("And user click on the house item")
    def item_info_is_visible(self, type_of_living, space):
        text = f"{type_of_living} {space}m\u00b2"
        el = self.find_element(ProfilePageLocators.HOUSE_ITEM_INFO)
        if el.text == text:
            return True


    @allure.step("And user click on the tariff item")
    def click_tariff_item(self):
        self.find_element_and_click(ProfilePageLocators.TARIFF_ITEM)

import allure
from pages.locators import DevicePageLocators
from pages.base_pages import BasePage


class DevicePage(BasePage):
    """Description """
    @allure.step("And user click on 'add new device' item ")
    def click_add_device(self):
        self.find_element_and_click(DevicePageLocators.ADD_DEVICE_ITEM)

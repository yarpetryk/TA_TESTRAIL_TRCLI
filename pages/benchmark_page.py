import allure
from selenium.webdriver.common.by import By
from pages.locators import BenchmarkPageLocators
from pages.base_pages import BasePage


class BenchmarkPage(BasePage):
    """Description """
    @allure.step("And user select the type of living")
    def select_type_of_living(self, type_of_living):
        self.find_all_elements(BenchmarkPageLocators.MENU_ITEM)[0].click()
        self.find_element_and_click((By.XPATH, BenchmarkPageLocators.TYPE_OF_LIVING_OPTION.format(type_of_living=type_of_living)))

    @allure.step("And user enter space")
    def enter_space_value(self, text):
        el = self.find_all_elements(BenchmarkPageLocators.MENU_ITEM)[1]
        el.clear() and el.send_keys(text)

    @allure.step("And user click on the user icon")
    def click_save_button(self):
        self.find_element_and_click(BenchmarkPageLocators.SAVE_BUTTON)

    @allure.step("And user accept pop-up")
    def accept_pop_up(self):
        self.find_element_and_click(BenchmarkPageLocators.ACCEPT_POP_UP_BUTTON)

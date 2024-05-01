import allure
from selenium.webdriver.common.by import By
from pages.locators import AnalyticsPageLocators
from pages.base_pages import BasePage


class AnalyticsPage(BasePage):
    """Description """
    @allure.step("And user click on the date picker")
    def click_date_picker(self):
        self.find_element_and_click(AnalyticsPageLocators.DATE_PICKER)

    @allure.step("And user click on the date picker")
    def click_device_picker(self):
        self.find_element_and_click(AnalyticsPageLocators.DEVICE_PICKER)

    @allure.step("And user click on the day tab on the calendar")
    def click_day_tab(self):
        el = self.find_element(AnalyticsPageLocators.CALENDAR_DAY_TAB)
        if not el.is_selected():
            el.click()

    @allure.step("And user select the day")
    def select_day(self, today, prev_day):
        current_day = today.split('.')[0]
        past_day = prev_day.split('.')[0]
        if int(current_day) - int(past_day) > 0:
            self.find_element_and_click((By.XPATH, AnalyticsPageLocators.DAY.format(day=past_day)))
        else:
            self.find_element_and_click(AnalyticsPageLocators.PREVIOUS_MONTH)
            self.find_element_and_click((By.XPATH, AnalyticsPageLocators.DAY.format(day=past_day)))

    @allure.step("And user close the calendar")
    def close_calendar(self):
        self.find_element_and_click(AnalyticsPageLocators.SAVE_BUTTON)

    @allure.step("And user check consumption sum")
    def check_consumption_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.CONSUMPTION_SUM, value)

    @allure.step("And user check feedIn sum")
    def check_feedIn_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.FEED_SUM, value)

    @allure.step("And user check generation sum")
    def check_generation_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.Production_SUM, value)

    @allure.step("And user check own consumption sum")
    def check_grid_consumption_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.GRID_CONSUMPTION_SUM, value)

    @allure.step("And user check own consumption sum")
    def check_own_consumption_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.OWN_CONSUMPTION_SUM, value)

    @allure.step("And user check total consumption sum")
    def check_total_consumption_sum(self, value):
        return self.check_element_equal(AnalyticsPageLocators.TOTAL_CONSUMPTION_SUM, value)

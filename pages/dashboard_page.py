import allure
from pages.locators import PowerMeterLocators
from pages.base_pages import BasePage


class DashboardPage(BasePage):
    """Description """
    @allure.step("And user check current power")
    def check_current_power(self, value):
        return self.check_element_equal(PowerMeterLocators.CURRENT_POWER, value)

    @allure.step("And user check power minimum")
    def check_power_minimum(self, value):
        return self.check_element_equal(PowerMeterLocators.MIN_POWER, value)

    @allure.step("And user check power average")
    def check_power_average(self, value):
        return self.check_element_equal(PowerMeterLocators.AVG_POWER, value)

    @allure.step("And user check power maximum")
    def check_power_maximum(self, value):
        return self.check_element_equal(PowerMeterLocators.MAX_POWER, value)

    @allure.step("And user check consumption sum")
    def check_consumption_sum(self, value):
        return self.check_element_equal(PowerMeterLocators.CONSUMPTION_SUM, value)

    @allure.step("And user check consumption currency")
    def check_consumption_currency(self, value):
        return self.check_element_equal(PowerMeterLocators.CONSUMPTION_CURRENCY, value)

    @allure.step("And user check consumption readings")
    def check_consumption_readings(self, value):
        el = self.find_element(PowerMeterLocators.CONSUMPTION_READINGS).text
        consumption_readings = el.replace('.', '')
        if value in consumption_readings:
            return True

    @allure.step("And user check feed sum")
    def check_feed_sum(self, value):
        return self.check_element_equal(PowerMeterLocators.FEED_SUM, value)

    @allure.step("And user check feed currency")
    def check_feed_currency(self, value):
        return self.check_element_equal(PowerMeterLocators.FEED_CURRENCY, value)

    @allure.step("And user check feed readings")
    def check_feed_readings(self, value):
        el = self.find_element(PowerMeterLocators.FEED_READINGS).text
        feed_readings = el.replace('.', '')
        if value in feed_readings:
            return True

    @allure.step("And user check generation sum")
    def check_generation_sum(self, value):
        return self.check_element_equal(PowerMeterLocators.GENERATION_SUM, value)

    @allure.step("And user check generation currency")
    def check_generation_currency(self, value):
        return self.check_element_equal(PowerMeterLocators.GENERATION_CURRENCY, value)

    @allure.step("And user check generation readings")
    def check_generation_readings(self, value):
        el = self.find_element(PowerMeterLocators.GENERATION_READINGS).text
        feed_readings = el.replace('.', '')
        if value in feed_readings:
            return True

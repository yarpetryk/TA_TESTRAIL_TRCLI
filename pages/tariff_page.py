import allure
from selenium.webdriver.common.by import By
from pages.locators import TariffPageLocators
from pages.base_pages import BasePage


class TariffPage(BasePage):
    """Description """
    @allure.step("And user click on the new tariff button")
    def click_new_tariff_button(self):
        self.find_element_and_click(TariffPageLocators.NEW_TARIFF_BUTTON)

    @allure.step("And user enter vendor name")
    def enter_vendor_name(self, text):
        self.find_element_and_send_key(TariffPageLocators.VENDOR_NAME_INPUT, text)

    @allure.step("And user enter tariff name")
    def enter_tariff_name(self, text):
        self.find_element_and_send_key(TariffPageLocators.TARIFF_NAME_INPUT, text)

    @allure.step("And user click on the next button")
    def click_next_button(self):
        self.find_element_and_click(TariffPageLocators.NEXT_BUTTON)


    @allure.step("And user select device")
    def select_device(self):
        self.find_element_and_click(TariffPageLocators.PROSUMER_DEVICE)

    @allure.step("And user enter basic price")
    def enter_basic_price(self, text):
        self.find_element_and_send_key(TariffPageLocators.BASIC_PRICE_INPUT, text)

    @allure.step("And user enter working price")
    def enter_working_price(self, text):
        self.find_element_and_send_key(TariffPageLocators.WORKING_PRICE_INPUT, text)

    @allure.step("And user enter prepayment")
    def enter_prepayment(self, text):
        self.find_element_and_send_key(TariffPageLocators.PREPAYMENT_INPUT, text)

    @allure.step("And user click on the calendar")
    def open_calendar(self):
        self.find_element_and_click(TariffPageLocators.CALENDAR)

    @allure.step("And user click on prev month button")
    def click_prev_month_button(self):
        self.find_element_and_click(TariffPageLocators.PREV_MONTH_BUTTON)

    @allure.step("And user select day")
    def select_day(self):
        self.find_element_and_click(TariffPageLocators.SELECT_DAY)

    @allure.step("And user close calendar")
    def close_calendar(self):
        self.find_element_and_click(TariffPageLocators.YES_BUTTON)

    @allure.step("And user click on the create tariff button")
    def click_create_tariff_button(self):
        self.find_element_and_click(TariffPageLocators.CREATE_TARIFF_BUTTON)

    @allure.step("And user close pop-up")
    def close_pop_up(self):
        self.find_element_and_click(TariffPageLocators.CLOSE_POP_UP)

    @allure.step("And user check vendor name")
    def check_vendor_name(self, value):
        return self.check_element_equal(TariffPageLocators.VENDOR_NAME, value)

    @allure.step("And user check tariff name")
    def check_tariff_name(self, value):
        return self.check_element_equal(TariffPageLocators.TARIFF_NAME, value)

    @allure.step("And user check tariff start date")
    def check_tariff_start_date(self, value):
        return self.check_element_equal(TariffPageLocators.TARIFF_START_DATE, value)

    @allure.step("And user check basic price")
    def check_basic_price(self, value):
        return self.check_element_equal(TariffPageLocators.BASIC_PRICE, value)

    @allure.step("And user check working price")
    def check_working_price(self, value):
        return self.check_element_equal(TariffPageLocators.WORKING_PRICE, value)

    @allure.step("And user check prepayment")
    def check_prepayment(self, value):
        return self.check_element_equal(TariffPageLocators.PREPAYMENT, value)

    @allure.step("And user click on the settings icon")
    def click_settings_icon(self):
        self.find_element_and_click(TariffPageLocators.SETTINGS_ICON)

    @allure.step("And user click on the delete fate button")
    def click_delete_rate(self):
        self.find_element_and_click(TariffPageLocators.DELETE_BUTTON)

    @allure.step("And user click on <yes> button")
    def confirm_deletion(self):
        self.find_element_and_click(TariffPageLocators.YES_BUTTON)

    @allure.step("And user check if tariff was removed")
    def check_tariff(self):
        return self.find_element(TariffPageLocators.PROSUMER_DEVICE)

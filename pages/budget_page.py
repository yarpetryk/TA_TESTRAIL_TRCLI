import allure
from selenium.webdriver.common.by import By
from pages.locators import BudgetPageLocators
from pages.base_pages import BasePage


class BudgetPage(BasePage):
    """Description """
    @allure.step("And user click on the date picker")
    def click_date_picker(self):
        self.find_element_and_click(BudgetPageLocators.DATE_PICKER)

    @allure.step("And user select the previous month")
    def select_prev_month(self, prev_month):
        month = prev_month.split()[0]
        self.find_element_and_click((By.XPATH, BudgetPageLocators.PREV_MONTH.format(month=month)))

    @allure.step("And user close the calendar")
    def close_calendar(self):
        self.find_element_and_click(BudgetPageLocators.CLOSE_CALENDAR)

    @allure.step("And user check prepayment")
    def check_prepayment(self, value):
        return self.check_element_equal(BudgetPageLocators.PREPAYMENT, value)

    @allure.step("And user check consumption")
    def check_consumption(self, value):
        return self.check_element_equal(BudgetPageLocators.CONSUMPTION, value)

    @allure.step("And user check percentage")
    def check_percentage(self, prepayment, consumption):
        a = consumption.replace(',', '.')
        b = prepayment.replace(',', '.')
        result = round((float(a) - float(b)), 2)
        if result < 0:
            value = f"{result}".replace('.', ',')
        elif result > 0:
            value = f"+{result}".replace('.', ',')
        else:
            value = 0
        return self.check_element_equal(BudgetPageLocators.PERCENTAGE, value)

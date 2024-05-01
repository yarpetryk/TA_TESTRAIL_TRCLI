import pytest
from api.api_budget import get_prepayment_current_month, get_prepayment_prev_month, get_consumption_current_month,\
    get_consumption_prev_month
from helpers.config_importer import ConfigImporter
from helpers.config_env import config_env
from helpers.get_date import get_month
from helpers.common_steps import swipe_down
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.dashboard_page import DashboardPage
from pages.budget_page import BudgetPage
from pages.tariff_page import TariffPage
from tests.test_login_and_select_prosumer_device import test_login


class TestBudget:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_importer = ConfigImporter()
        self.config_env = config_env()
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.budget_page = BudgetPage(self.driver)
        self.tariff_page = TariffPage(self.driver)
        self.login = self.config_env['login']
        self.password = self.config_env['password']
        self.prev_month = get_month().get('prev_month')
        self.prev_month_tariff = get_month().get('prev_month_tariff')
        self.current_month = get_month().get('current_month')
        self.tariff_input_data = {
            "vendor_name": "Power vendor",
            "tariff_name": "Basic tariff",
            "basic_price": "10",
            "working_price": "2",
            "prepayment": "25"
        }

        # Mark test as a "create_tariff" to run marked tests in the future

    @pytest.mark.create_tariff
    def test_create_tariff(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on User icon
        self.home_page.click_user_icon()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on Tariff item
        self.profile_page.click_tariff_item()

        # The User click on create new tariff button
        self.tariff_page.click_new_tariff_button()

        # The User enter vendor name
        self.tariff_page.enter_vendor_name(self.tariff_input_data['vendor_name'])

        # The User enter tariff name
        self.tariff_page.enter_tariff_name(self.tariff_input_data['tariff_name'])

        # The User click on next button
        self.tariff_page.click_next_button()

        # The user select <prosumer> device
        self.tariff_page.select_device()

        # The User enter basic price
        self.tariff_page.enter_basic_price(self.tariff_input_data['basic_price'])

        # The User enter working price
        self.tariff_page.enter_working_price(self.tariff_input_data['working_price'])

        # The User enter prepayment
        self.tariff_page.enter_prepayment(self.tariff_input_data['prepayment'])

        # The User open calendar
        self.tariff_page.open_calendar()

        # The User go to previous month
        self.tariff_page.click_prev_month_button()

        # The User select day
        self.tariff_page.select_day()

        # The User close calendar
        self.tariff_page.close_calendar()

        # The User click on next button
        self.tariff_page.click_next_button()

        # The user swipe down
        swipe_down(self.driver)

        # The User click on create tariff button
        self.tariff_page.click_create_tariff_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User close pop-up
        self.tariff_page.close_pop_up()

        # The user check vendor name
        assert self.tariff_page.check_vendor_name(self.tariff_input_data['vendor_name'])

        # The user check tariff name
        assert self.tariff_page.check_tariff_name(self.tariff_input_data['tariff_name'])

        # The user check tariff start date
        assert self.tariff_page.check_tariff_start_date(self.prev_month_tariff)

        # The user check basic price
        assert self.tariff_page.check_basic_price(self.tariff_input_data['basic_price'])

        # The user check working price
        assert self.tariff_page.check_working_price(self.tariff_input_data['working_price'])

        # The user check prepayment
        assert self.tariff_page.check_prepayment(self.tariff_input_data['prepayment'])

    # Mark test as a "budget" to run marked tests in the future
    @pytest.mark.budget
    def test_budget(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API calls
        self.prepayment_current_month = get_prepayment_current_month(self.login, self.password)
        self.prepayment_prev_month = get_prepayment_prev_month(self.login, self.password)
        self.consumption_current_month = get_consumption_current_month(self.login, self.password)
        self.consumption_prev_month = get_consumption_prev_month(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user select the Analytics tab
        self.home_page.select_budget_tab()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User check <prepayment> value
        assert self.budget_page.check_prepayment(self.prepayment_current_month['prepayment']), \
            f"API response: {self.prepayment_current_month['prepayment']}"

        # The User check <consumption> value
        assert self.budget_page.check_consumption(self.consumption_current_month['consumption']), \
            f"API response: {self.consumption_current_month['consumption']}"

        # The User check <percentage> value
        assert self.budget_page.check_percentage(self.prepayment_current_month['prepayment'],
                                                 self.consumption_current_month['consumption'])

        # The user select the date picker
        self.budget_page.click_date_picker()

        # The user select the previous month
        self.budget_page.select_prev_month(self.prev_month)

        # The user close calendar
        self.budget_page.close_calendar()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User check <prepayment> value
        assert self.budget_page.check_prepayment(self.prepayment_prev_month['prepayment']),\
            f"API response: {self.prepayment_prev_month['prepayment']}"

        # The User check <consumption> value
        assert self.budget_page.check_consumption(self.consumption_prev_month['consumption']),\
            f"API response: {self.consumption_prev_month['consumption']}"

        # The User check <percentage> value
        assert self.budget_page.check_percentage(self.prepayment_prev_month['prepayment'],self.consumption_prev_month['consumption'])

    # Mark test as a "delete_tariff" to run marked tests in the future
    @pytest.mark.delete_tariff
    def test_delete_tariff(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on User icon
        self.home_page.click_user_icon()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on Tariff item
        self.profile_page.click_tariff_item()

        # The User click on settings item
        self.tariff_page.click_settings_icon()

        # The User click on delete rate button
        self.tariff_page.click_delete_rate()

        # The User confirm the rate removing
        self.tariff_page.confirm_deletion()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user check if rate was removed
        assert not self.tariff_page.check_tariff()

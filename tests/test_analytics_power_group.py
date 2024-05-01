import pytest
from pages.analytics_page import AnalyticsPage
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from api.api_analytics import power_group_analytics
from tests.test_login_and_select_generator_device import test_login
from helpers.config_env import config_env
from helpers.get_date import past_date


class TestAnalyticsPower:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_env = config_env()
        self.analytics_page = AnalyticsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.login = self.config_env['login']
        self.password = self.config_env['password']
        self.today = past_date().get('current_date')
        self.prev_day = past_date().get('past_date')

    # Mark test as a "power_operating" to run marked tests in the future
    @pytest.mark.analytics_power_group
    def test_analytics_power_group(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API call
        self.power_group_value = power_group_analytics(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user select the Analytics tab
        self.home_page.select_analytics_tab()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user click on <device picker>
        self.analytics_page.click_device_picker()

        # The user select <Alle Strom>
        self.home_page.select_power_group()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user select the date picker
        self.analytics_page.click_date_picker()

        # The user select the day tab
        self.analytics_page.click_day_tab()

        # The user select the day
        self.analytics_page.select_day(self.today, self.prev_day)

        # The user close the calendar
        self.analytics_page.close_calendar()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User check <consumption sum> value
        assert self.analytics_page.check_grid_consumption_sum(self.power_group_value['consumption_sum']),\
            f"API response: {self.power_group_value['consumption_sum']}"

        # The User check <own consumption> value
        assert self.analytics_page.check_own_consumption_sum(self.power_group_value['own_consumption_sum']),\
            f"API response: {self.power_group_value['own_consumption_sum']}"
            
        # The User check <total consumption> value
        assert self.analytics_page.check_total_consumption_sum(self.power_group_value['total_consumption_sum']),\
            f"API response: {self.power_group_value['total_consumption_sum']}"

import pytest
from pages.analytics_page import AnalyticsPage
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from api.api_analytics import prosumer_analytics
from tests.test_login_and_select_prosumer_device import test_login
from helpers.config_env import config_env
from helpers.get_date import past_date
import trcli


class TestAnalyticsProsumer:
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
    @pytest.mark.analytics_prosumer
    def test_analytics_prosumer(self, driver, record_property):
        record_property("test_id", "C568")
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API call
        self.prosumer_value = prosumer_analytics(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user select the Analytics tab
        self.home_page.select_analytics_tab()

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
        assert self.analytics_page.check_consumption_sum(self.prosumer_value['consumption_sum'])

        # The User check <feedIn> value
        assert self.analytics_page.check_feedIn_sum(self.prosumer_value['consumption_sum'])

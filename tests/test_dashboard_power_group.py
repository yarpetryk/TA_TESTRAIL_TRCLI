import pytest
from api.api_operating import power_group_operating
from api.api_summary import power_group_summary
from helpers.config_importer import ConfigImporter
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from tests.test_login_and_select_power_group import test_login
from helpers.config_env import config_env


class TestPower:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_env = config_env()
        self.config_importer = ConfigImporter()
        self.home_page = HomePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.login = self.config_env['login']
        self.password = self.config_env['password']


    # Mark test as a "power_operating" to run marked tests in the future
    @pytest.mark.power_operating
    def test_power_operating(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # Execute API call
        self.power_operating_value = power_group_operating(self.login, self.password)

        # The User check <current power> value
        assert self.dashboard_page.check_current_power(self.power_operating_value['current_power']),\
            f"API response: {self.power_operating_value['current_power']}"

        # The User check <power minimum> value
        assert self.dashboard_page.check_power_minimum(self.power_operating_value['minimum']),\
            f"API response: {self.power_operating_value['minimum']}"

        # The User check <power average> value
        assert self.dashboard_page.check_power_average(self.power_operating_value['average']),\
            f"API response: {self.power_operating_value['average']}"

        # The User check <power maximum> value
        assert self.dashboard_page.check_power_maximum(self.power_operating_value['maximum']),\
            f"API response: {self.power_operating_value['maximum']}"

    # Mark test as a "power_summary" to run marked tests in the future
    @pytest.mark.power_summary
    def test_power_summary(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API call
        self.power_summary_value = power_group_summary(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User check <consumption sum> value
        assert self.dashboard_page.check_consumption_sum(self.power_summary_value['consumption_sum']),\
            f"API response: {self.power_summary_value['consumption_sum']}"

        # The User check <consumption currency> value
        assert self.dashboard_page.check_consumption_currency(self.power_summary_value['consumption_currency']),\
            f"API response: {self.power_summary_value['consumption_currency']}"

        # The User check <feed sum> value
        assert self.dashboard_page.check_feed_sum(self.power_summary_value['feed_sum']),\
            f"API response: {self.power_summary_value['feed_sum']}"

        # The User check <feed currency> value
        assert self.dashboard_page.check_feed_currency(self.power_summary_value['feed_currency']),\
            f"API response: {self.power_summary_value['feed_currency']}"


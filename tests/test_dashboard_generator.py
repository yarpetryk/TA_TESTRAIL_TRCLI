import pytest
from api.api_operating import generator_operating
from api.api_summary import generator_summary
from helpers.config_importer import ConfigImporter
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from tests.test_login_and_select_generator_device import test_login
from helpers.config_env import config_env


class TestGenerator:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_env = config_env()
        self.config_importer = ConfigImporter()
        self.home_page = HomePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.login = self.config_env['login']
        self.password = self.config_env['password']

    # Mark test as a "generator_operating" to run marked tests in the future
    @pytest.mark.generator_operating
    def test_generator_operating(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API call
        self.power_operating_value = generator_operating(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

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

    # Mark test as a "generator_summary" to run marked tests in the future
    @pytest.mark.generator_summary
    def test_generator_summary(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # Execute API call
        self.power_summary_value = generator_summary(self.login, self.password)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User check <generation sum> value
        assert self.dashboard_page.check_generation_sum(self.power_summary_value['generation_sum']),\
            f"API response: {self.power_summary_value['generation_sum']}"

        # The User check <generation currency> value
        #assert self.dashboard_page.check_generation_currency(self.power_summary_value['generation_currency']),\
            #f"API response: {self.power_summary_value['generation_currency']}"

        # The User check <generation readings> value
        assert self.dashboard_page.check_generation_readings(self.power_summary_value['generation_readings']),\
            f"API response: {self.power_summary_value['generation_readings']}"

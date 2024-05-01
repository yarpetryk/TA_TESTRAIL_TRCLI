import pytest
from pages.home_page import HomePage
from helpers.config_importer import ConfigImporter
from helpers.get_date import current_date
from tests.test_login_and_select_prosumer_device import test_login


class TestDate:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_importer = ConfigImporter()
        self.home_page = HomePage(self.driver)
        self.date = current_date(self.config_importer.config_language(), self.config_importer.config_locale())

    # Mark test as a "date" to run marked tests in the future
    @pytest.mark.date
    def test_date(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # The User see the date
        assert self.home_page.date_is_visible(self.date)

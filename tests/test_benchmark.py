import pytest
import random
from helpers.config_importer import ConfigImporter
from helpers.get_date import current_date
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.benchmark_page import BenchmarkPage
from tests.test_login_and_select_prosumer_device import test_login


class TestBenchmark:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_importer = ConfigImporter()
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.benchmark_page = BenchmarkPage(self.driver)
        self.date = current_date(self.config_importer.config_language(), self.config_importer.config_locale())

    # Mark test as a "profile" to run marked tests in the future
    @pytest.mark.profile
    def test_benchmark(self, driver):
        #  Initialization
        self.init(driver)
        type_of_living = "Wohnung"
        space = random.randrange(100, 1000, 10)

        # The user login
        test_login(driver)

        # The User see the date
        assert self.home_page.date_is_visible(self.date)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on User icon
        self.home_page.click_user_icon()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User see Log out menu item
        assert self.profile_page.log_out_menu_item_is_visible()

        # The User click on House item
        self.profile_page.click_house_item()

        # The User select the type of living
        self.benchmark_page.select_type_of_living(type_of_living)

        # The User enter the space value
        self.benchmark_page.enter_space_value(space)

        # The User click save button
        self.benchmark_page.click_save_button()

        # The User click OK button on pop-up
        self.benchmark_page.accept_pop_up()

        # The User can see house item info
        assert self.profile_page.item_info_is_visible(type_of_living, space)

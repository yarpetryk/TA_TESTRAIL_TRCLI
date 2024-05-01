import time
import pytest
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from tests.test_login_and_select_prosumer_device import test_login


class TestProfile:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    # Mark test as a "profile" to run marked tests in the future
    @pytest.mark.profile
    def test_navigate_to_profile_page(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)
        time.sleep(2)

        # The User click on User Icon
        self.home_page.click_user_icon()

        # The User see Log out menu item
        assert self.profile_page.log_out_menu_item_is_visible()


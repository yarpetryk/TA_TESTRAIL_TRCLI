import pytest
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.device_page import DevicePage
from tests.test_login_and_select_prosumer_device import test_login


class TestDeviceActivation:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.device_page = DevicePage(self.driver)

    # Mark test as a "profile" to run marked tests in the future
    @pytest.mark.device_activate
    def test_device_activate(self, driver):
        #  Initialization
        self.init(driver)

        # The user login
        test_login(driver)

        # The User click on User icon
        self.home_page.click_user_icon()

        # The User click on Device item
        self.profile_page.click_device_item()

        # The User click on Add device item
        self.device_page.click_add_device()



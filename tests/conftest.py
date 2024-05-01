import pytest
from appium import webdriver
from helpers.config_importer import ConfigImporter


config_importer = ConfigImporter()

@pytest.fixture(scope="function")
def driver(record_property):
    locale = str(config_importer.config_locale())
    language = str(config_importer.config_language())
    capabilities = {
        'platformName': 'Android',
        'language': language,
        'locale': locale
    }
    url = 'http://localhost:4723/wd/hub'
    appium_driver = webdriver.Remote(url, capabilities)
    appium_driver.get_screenshot_as_file("image.png")
    record_property("testrail_attachment", "image.png")
    yield appium_driver
    appium_driver.quit()


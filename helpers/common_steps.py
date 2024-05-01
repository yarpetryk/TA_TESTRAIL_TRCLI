from helpers.adb_commands import *
import time
from helpers.config_importer import ConfigImporter


def uninstall_app(driver):
    config_importer = ConfigImporter()
    driver.remove_app(str(config_importer.config_package_name()))


def terminate_app(driver):
    config_importer = ConfigImporter()
    driver.terminate_app(str(config_importer.config_package_name()))


def is_installed(driver):
    config_importer = ConfigImporter()
    return driver.is_app_installed(str(config_importer.config_package_name()))


def activate_app(driver):
    config_importer = ConfigImporter()
    driver.activate_app(str(config_importer.config_package_name()))
    time.sleep(2)


def clear_data_and_run_app(driver, clear_data=True):
    config_importer = ConfigImporter()
    if clear_data:
        clear_app_data(str(config_importer.config_package_name()))
    driver.activate_app(str(config_importer.config_package_name()))
    time.sleep(2)


def open_notification(driver):
    driver.open_notifications()


def swipe_down(driver):
    driver.swipe(0, 500, 0, 0)

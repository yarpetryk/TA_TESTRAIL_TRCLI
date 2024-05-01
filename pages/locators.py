from selenium.webdriver.common.by import By


class PowerMeterLocators(object):
    """A class for Power Dashboard page locators. All Power Dashboard locators should come here"""
    CURRENT_POWER = (By.XPATH, "//*[contains(@resource-id,'tv_value_watt')]")
    MIN_POWER = (By.XPATH, "//*[contains(@resource-id,'tv_value_avg')]/preceding-sibling::*[last()]")
    AVG_POWER = (By.XPATH, "//*[contains(@resource-id,'tv_value_avg')]")
    MAX_POWER = (By.XPATH, "//*[contains(@resource-id,'tv_value_avg')]/following-sibling::*[position()=1]")
    CONSUMPTION_SUM = (By.XPATH, "//*[contains(@text,'Verbrauch')]/following-sibling::*[contains(@resource-id,'tv_summary_generation_sum')]")
    CONSUMPTION_CURRENCY = (By.XPATH, "//*[contains(@text,'Verbrauch')]/following-sibling::*[contains(@resource-id,'tv_sum_currency')]")
    CONSUMPTION_READINGS = (By.XPATH, "//*[contains(@text,'Verbrauch')]/following-sibling::*[contains(@resource-id,'tv_summary_generation_value')]")
    FEED_SUM = (By.XPATH, "//*[contains(@text,'Einspeisung')]/following-sibling::*[contains(@resource-id,'tv_summary_generation_sum')]")
    FEED_CURRENCY = (By.XPATH, "//*[contains(@text,'Einspeisung')]/following-sibling::*[contains(@resource-id,'tv_sum_currency')]")
    FEED_READINGS = (By.XPATH, "//*[contains(@text,'Einspeisung')]/following-sibling::*[contains(@resource-id,'tv_summary_generation_value')]")
    GENERATION_SUM = (By.XPATH, "//*[contains(@resource-id,'tv_summary_generation_sum')]")
    GENERATION_CURRENCY = (By.XPATH, "//*[contains(@resource-id,'tv_summary_generation_sum')]/following-sibling::*[position()=1]")
    GENERATION_READINGS = (By.XPATH, "//*[contains(@resource-id,'tv_summary_generation_value')]")


class HomePageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    USER_ICON = (By.XPATH, "//*[contains(@resource-id,'ll_top_icons')]/child::*[position()=2]")
    CURRENT_DATE = (By.XPATH, "//*[contains(@resource-id,'cl_selector_calendar')]")
    NAV_BAR = (By.XPATH, "//*[contains(@resource-id,'bottom_nav')]")
    DEVICE_PROSUMER = (By.XPATH, "//*[contains(@text,'prosumer')]")
    DEVICE_GENERATOR = (By.XPATH, "//*[contains(@text,'generator')]")
    DEVICE_POWER_GROUP = (By.XPATH, "//*[contains(@text,'Alle Strom')]")
    SPINNER = (By.CLASS_NAME, "android.widget.ProgressBar")
    ANALYTICS_TAB = (By.XPATH, "//*[contains(@resource-id,'tabAnalyticsFragment')]")
    BUDGET_TAB = (By.XPATH, "//*[contains(@resource-id,'tabPercentFragment')]")


class AnalyticsPageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    DATE_PICKER = (By.XPATH, "//*[contains(@resource-id,'cl_selector_calendar')]")
    DEVICE_PICKER = (By.XPATH, "//*[contains(@resource-id,'cl_selected_device')]")
    CALENDAR_DAY_TAB = (By.XPATH, "//*[contains(@resource-id,'ll_selector')]/child::*[position()=2]")
    DAY = "//*[contains(@resource-id,'month_view')]/child::*[position()={day}]"
    SAVE_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_button_second')]")
    PREVIOUS_MONTH = (By.XPATH, "//*[contains(@resource-id,'prev')]")
    CONSUMPTION_SUM = (By.XPATH, "//*[starts-with(@text,'Verbrauch')]/following-sibling::*[position()=1]")
    FEED_SUM = (By.XPATH, "//*[contains(@text,'Einspeisung')]/following-sibling::*[position()=1]")
    Production_SUM = (By.XPATH, "//*[contains(@text,'Produktion')]/following-sibling::*[position()=1]")
    OWN_CONSUMPTION_SUM = (By.XPATH, "//*[starts-with(@text,'Verbrauch Eigenproduktion')]/following-sibling::*[position()=1]")
    GRID_CONSUMPTION_SUM = (By.XPATH, "//*[starts-with(@text,'Netzverbrauch')]/following-sibling::*[position()=1]")
    TOTAL_CONSUMPTION_SUM = (By.XPATH, "//*[starts-with(@text,'Gesamtverbrauch')]/following-sibling::*[position()=1]")


class RegisterPageLocators(object):
    """A class for Bot page locators. All Start page locators should come here"""
    INPUT_FIELD = (By.CLASS_NAME, "android.widget.EditText")
    REGISTER_BUTTON = (By.XPATH, "//*[contains(@text,'Register')]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_login')]")
    USER_REGISTERED = (By.XPATH, "//*[contains(@text,'Verify your e-mail')]")
    USER_ALREADY_REGISTERED = (By.XPATH, "//*[contains(@text,'E-Mail-Adresse bereits als Benutzerkonto registriert')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(@resource-id,'textinput_error')]")


class LoginPageLocators(object):
    """A class for Bot page locators. All Login page locators should come here"""
    #USERNAME_FIELD = (By.XPATH, "//*[contains(@resource-id,'Username')]")
    #PASSWORD_FIELD = (By.XPATH, "//*[contains(@resource-id,'Password')]")
    #LOGIN_BUTTON = (By.CLASS_NAME, "android.widget.Button")
    USERNAME_FIELD = (By.CLASS_NAME, "android.widget.EditText")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/following-sibling::*[position()=1]")
    ERROR_MESSAGE = "//*[@text = '{name}']"
    SKIP_BUTTON = (By.XPATH, "//*[contains(@text,'Überspringen')]")
    SKIP_ACTIVATION_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_activate_device_2_button')]")


class ProfilePageLocators(object):
    """A class for Bot page locators. All Profile page locators should come here"""
    LOG_OUT_ITEM = (By.XPATH, "//*[contains(@resource-id,'cl_log_out')]")
    GEAR_ICON = (By.XPATH, "//*[contains(@resource-id,'iv_settings')]")
    HOUSE_ITEM = (By.XPATH, "//*[contains(@resource-id,'rv_long_cut')]/child::*[position()=1]")
    DEVICE_ITEM = (By.XPATH, "//*[contains(@resource-id,'rv_long_cut')]/child::*[position()=2]")
    HOUSE_ITEM_INFO = (By.XPATH, "//*[contains(@resource-id,'rv_long_cut')]/child::*[position()=1]/*[contains(@resource-id,'tv_value')]")
    TARIFF_ITEM = (By.XPATH, "//*[contains(@resource-id,'rv_long_cut')]/child::*[position()=3]")


class ProfileSettingsPageLocators(object):
    """A class for Bot page locators. All Edit Profile page locators should come here"""
    RESET_PASSWORD_ITEM = (By.XPATH, "//*[contains(@resource-id,'tv_change_password')]")


class ResetPasswordLocators(object):
    """A class for Bot page locators. All Reset password locators should come here"""
    TITLE = (By.XPATH, "//*[contains(@resource-id,'tv_edit_profile')]")
    INPUT_FIELD = (By.CLASS_NAME, "android.widget.EditText")
    SAVE_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_save_button')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(@resource-id,'textinput_error')]")
    PASSWORD_UPDATED_POP_UP_TITLE = (By.XPATH, "//*[contains(@resource-id,'tv_title')]")


class BenchmarkPageLocators(object):
    """A class for Bot page locators. All Benchmark locators should come here"""
    MENU_ITEM = (By.CLASS_NAME, "android.widget.EditText")
    TYPE_OF_LIVING_OPTION = "//*[@text = '{type_of_living}']"
    SAVE_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_save_button')]")
    ACCEPT_POP_UP_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_button')]")


class DevicePageLocators(object):
    """A class for Bot page locators. All Device locators should come here"""
    ADD_DEVICE_ITEM = (By.XPATH, "//*[contains(@text,'+')]")

class BudgetPageLocators(object):
    """A class for Budget page locators. All DBudget locators should come here"""
    PREPAYMENT = (By.XPATH, "//*[contains(@text,'Monatsabschlag')]/following-sibling::*[position()=1]")
    CONSUMPTION = (By.XPATH, "//*[contains(@text,'Monatskosten')]/following-sibling::*[position()=1]")
    PERCENTAGE = (By.XPATH, "//*[contains(@text,'+/-')]/following-sibling::*[position()=1]")
    DATE_PICKER = (By.XPATH, "//*[contains(@resource-id,'tv_current_day_date')]")
    PREV_MONTH = "//*[@text = '{month}']"
    CLOSE_CALENDAR = (By.XPATH, "//*[contains(@resource-id,'tv_button_second')]")


class TariffPageLocators(object):
    """A class for Budget page locators. All DBudget locators should come here"""
    NEW_TARIFF_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_add_new_tariff_button')]")
    VENDOR_NAME_INPUT = (By.XPATH, "//*[contains(@text,'Anbietername')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    TARIFF_NAME_INPUT = (By.XPATH, "//*[contains(@text,'Tarifbezeichnung')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    BASIC_PRICE_INPUT = (By.XPATH, "//*[contains(@text,'Basispreis')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    WORKING_PRICE_INPUT = (By.XPATH, "//*[contains(@text,'Arbeitspreis')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    PREPAYMENT_INPUT = (By.XPATH, "//*[contains(@text,'Abschlag')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    NEXT_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_abort_button')]/following-sibling::*[position()=1]")
    CALENDAR = (By.XPATH, "//*[contains(@text,'Tarif Startdatum')]/following-sibling::*[position()=1]/child::*[position()=1]/child::*[position()=1]")
    PREV_MONTH_BUTTON = (By.XPATH, "//*[contains(@resource-id,'prev')]")
    SELECT_DAY = ( By.XPATH, "//*[contains(@resource-id,'month_view')]/child::*[position()=1]")
    CREATE_TARIFF_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_save_tariff_button')]")
    CLOSE_POP_UP = (By.XPATH, "//*[contains(@resource-id,'tv_button')]")
    PROSUMER_DEVICE = (By.XPATH, "//*[contains(@text,'prosumer')]")
    VENDOR_NAME = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=2]")
    TARIFF_NAME = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=3]")
    TARIFF_START_DATE = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=4]")
    BASIC_PRICE = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=8]")
    WORKING_PRICE = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=9]")
    PREPAYMENT = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=13]")
    SETTINGS_ICON = (By.XPATH, "//*[contains(@text,'prosumer')]/following-sibling::*[position()=1]")
    DELETE_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_button')]")
    YES_BUTTON = (By.XPATH, "//*[contains(@resource-id,'tv_button_second')]")


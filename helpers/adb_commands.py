import os
import allure
################################### ADB COMMANDS SECTION #############################

def get_device_serial(device_serial_id) -> str:
    """
    Purpose:
        Returns the device serial of the currently running device for this test
    Args:
        device_serial id(str): (eg: c743b9af267cc3f2)
    Returns:
        str
    """
    if not device_serial_id:
        return 'No Device found'
    command = 'adb -s ' + str(device_serial_id) + ' shell getprop ril.serialnumber'
    device_serial = os.popen(command).read()
    return str(device_serial)

def get_connected_device_serial() -> str:
    """
    Purpose:
        Returns connected device serial
    Returns:
        str
    """
    command = 'adb devices -l'
    device_serial = os.popen(command).read()
    return device_serial.splitlines()[1].split(' ')[0].strip(' ')

def get_hos_app_version_on_connected_device():
    """
        Purpose:
            Returns hos app version
        Returns:
            str
        """
    if os.name == 'posix':
        command = 'adb shell dumpsys package com.pltsci.hos | grep versionName'
    else:
        command = 'adb shell dumpsys package com.pltsci.hos | findstr versionName'
    hos_version = os.popen(command).read()
    if not hos_version:
        return 'Not installed\n'
    return hos_version.replace('    versionName=','')

def get_device_model_type(device_serial_id) -> str:
    """
    Purpose:
        Returns the device model type of the currently running device for this test
    Args:
        device_serial id(str): (eg: c743b9af267cc3f2)
    Returns:
        str
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell getprop ro.product.model'
    try:
        tablet_type = os.popen(command).read()
    except Exception:
        return "cannot retrieve tablet type"
    else:
        return str(tablet_type)

def get_android_version(device_serial_id):
    command = 'adb -s ' + str(device_serial_id) + ' shell getprop ro.build.version.release'
    android_version = os.popen(command).read()
    return str(android_version)


def clear_app_data(app_package_name:str):
    """
    Purpose:
        Clear the app data for the specified app
    Args:
        device_serial id(str): pass in pytest.device_name
        app_package_name(str): the package name of the app. ex: "com.pltsci.hos"
    Returns:
        None
    """

    command = 'adb shell pm clear ' + str(app_package_name)
    try:
        success_message = os.popen(command).read()
    except Exception:
        pass
    else:
        print(f"clearing app data of {app_package_name} is {success_message}")

@allure.step("And force stop {app_package_name}")
def app_force_stop(device_serial_id:str, app_package_name:str):
    """
    Purpose:
        Use to force stop the app proccess
    """

    command = 'adb -s ' + str(device_serial_id) + ' shell am force-stop ' + str(app_package_name)
    os.popen(command).read()

def turn_on_wifi(device_serial_id):
    """
    Purpose:
        Turn the WIFI on
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell "svc wifi enable" '
    os.popen(command).read()
    print(command)

def turn_on_airplane_mode(device_serial_id):
    """
    Purpose:
        Turn the airplane mode on for disabling the Bluetooth
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell settings put global airplane_mode_on 1 '
    os.popen(command).read()
    print(command)

def turn_off_airplane_mode(device_serial_id):
    """
    Purpose:
        Turn the airplane mode off for disabling the Bluetooth
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell settings put global airplane_mode_on 0 '
    os.popen(command).read()
    print(command)

def get_app_version(device_id, app) -> str:
    command = 'adb -s ' + str(device_id) + \
            ' shell dumpsys package com.pltsci.{0} | grep versionName'.format(app)
    app_version = os.popen(command).read()
    version_number = app_version.replace('    versionName=','')
    if not version_number:
        return 'Not installed\n'
    return app_version.replace('    versionName=','')

app_list = [
    'hos',
    'pscore',
    'orion launcher',
    'orion push notifications',
    'application manager',
    'dvir',
    'workflow',
    'wifi manager',
    'messaging',
    'navigation',
    'driver performance',
    'connection']

@allure.step("And open locale(language) settings on the Android")
def open_android_locale_settings(device_serial_id):
    """
    Purpose:
        Open the locale settings on Android
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell am start -a android.settings.LOCALE_SETTINGS '
    os.popen(command).read()
    print(command)

@allure.step("And we set {country} language ")
def set_locale_language(device_serial_id, lang, country):
    """
        Purpose:
            Set locale to Android
            Example : adb shell am broadcast -a io.appium.settings.locale --es lang en --es country US
        """
    command = 'adb -s ' + str(device_serial_id) + f' shell am broadcast -a io.appium.settings.locale --es lang {lang} --es country {country}'
    os.popen(command).read()
    print(command)

@allure.step("And we open the date and time settings")
def open_date_time_settings(device_serial_id):
    """
        Purpose:
            Open the date and time settings on Android
        """
    command = 'adb -s ' + str(device_serial_id) + ' shell am start -a android.settings.DATE_SETTINGS '
    os.popen(command).read()
    print(command)

@allure.step("And we force close settings")
def close_settings(device_serial_id):
    """
    Purpose:
        Force closes settings
    """
    command = 'adb -s ' + str(device_serial_id) + ' shell am force-stop com.android.settings '
    os.popen(command).read()
    print(command)

@allure.step("And we get the device volume")
def get_device_volume(device_serial_id, audio_stream_index) -> str:
    command = 'adb -s ' + str(device_serial_id) + ' shell media volume --stream ' + str(audio_stream_index) + ' --get'
    device_volume = os.popen(command).read()
    return device_volume.splitlines()[3].split(' ')[3].strip(' ')

@allure.step("And we install app")
def install_app(path_to_apk):
    command = 'adb install ' + str(path_to_apk)
    os.popen(command).read()

@allure.step("And we uninstall app")
def uninstall_app(app_package):
    command = 'adb uninstall ' + str(app_package)
    os.popen(command).read()

################################### ADB COMMANDS SECTION #############################


import requests
from math import ceil
from requests.auth import HTTPBasicAuth
from helpers.config_env import config_env


def power_operating_value(value):
    if round(value) in range(-999, 1000):
        return str(round(abs(value)))
    else:
        value_1 = round(abs(value)/1000, 2)
        value_2 = round(abs(value)/1000, 3)
        result = round((value_2-value_1)*1000)
        if result == 5:
            value = ceil(value/10)/100
        else:
            value = round(abs(value)/1000, 2)
        return f"{value: .2f}".replace('.', ',')


def prosumer_operating(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "extended": True
    }
    url = f"{base_url}/current/0/operating"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    current_power = power_operating_value(data['watt']).strip()
    minimum = power_operating_value(data['min']).strip()
    maximum = power_operating_value(data['max']).strip()
    average = power_operating_value(data['avg']).strip()

    return {
        "current_power": current_power,
        "minimum": minimum,
        "maximum": maximum,
        "average": average
    }


def generator_operating(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-GENERATE-LEMBERG",
        "extended": True
    }
    url = f"{base_url}/current/0/operating"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    current_power = power_operating_value(data['watt']).strip()
    minimum = power_operating_value(data['min']).strip()
    maximum = power_operating_value(data['max']).strip()
    average = power_operating_value(data['avg']).strip()

    return {
        "current_power": current_power,
        "minimum": minimum,
        "maximum": maximum,
        "average": average
    }


def power_group_operating(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "division": 0,
        "mainDevice": True,
        "extended": True
    }
    url = f"{base_url}/current/0/operating"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    current_power = power_operating_value(data['watt']).strip()
    minimum = power_operating_value(data['min']).strip()
    maximum = power_operating_value(data['max']).strip()
    average = power_operating_value(data['avg']).strip()

    return {
        "current_power": current_power,
        "minimum": minimum,
        "maximum": maximum,
        "average": average
    }

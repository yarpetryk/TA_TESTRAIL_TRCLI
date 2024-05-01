import requests
from math import ceil
from requests.auth import HTTPBasicAuth
from helpers.config_env import config_env


def power_summary_value(value, meter_readings=False):
    if meter_readings:
        return str(round(value/1000))

    if isinstance(value, int):
        if value == 0:
            return f"{value: .2f}".replace('.', ',')
        else:
            return str(value)
    else:
        value_1 = round(value, 2)
        value_2 = int(value * 1000) / 1000
        result = round((value_2 - value_1) * 1000)
        if result == 5:
            value = f"{value: g}"
        else:
            value = round(value, 2)
        return f"{value: .2f}".replace('.', ',')


def prosumer_summary(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER"
    }
    url = f"{base_url}/current/0/summary"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Consumption values
    consumption_sum = power_summary_value(data['consumption']['sum']).strip()
    consumption_currency = power_summary_value(data['consumption']['sumCurrency']).strip()
    consumption_readings = power_summary_value(data['consumption']['meterReadings'][0]['value'], meter_readings=True)

    # FeedIn values
    feed_sum = power_summary_value(data['feedIn']['sum']).strip()
    feed_currency = power_summary_value(data['feedIn']['sumCurrency']).strip()
    feed_readings = power_summary_value(data['feedIn']['meterReadings'][0]['value'], meter_readings=True)

    return {
        "consumption_sum": consumption_sum,
        "consumption_currency": consumption_currency,
        "consumption_readings": consumption_readings,
        "feed_sum": feed_sum,
        "feed_currency": feed_currency,
        "feed_readings": feed_readings
    }


def generator_summary(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-GENERATE-LEMBERG"
    }
    url = f"{base_url}/current/0/summary"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Generation values
    generation_sum = power_summary_value(data['generation']['sum']).strip()
    generation_currency = power_summary_value(data['generation']['sumCurrency']).strip()
    generation_readings = power_summary_value(data['generation']['meterReadings'][0]['value'], meter_readings=True)

    return {
        "generation_sum": generation_sum,
        "generation_currency": generation_currency,
        "generation_readings": generation_readings
    }


def power_group_summary(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "division": 0,
        "mainDevice": True
    }
    url = f"{base_url}/current/0/summary"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Consumption values
    consumption_sum = power_summary_value(data['consumption']['sum']).strip()
    consumption_currency = power_summary_value(data['consumption']['sumCurrency']).strip()

    # FeedIn values
    feed_sum = power_summary_value(data['feedIn']['sum']).strip()
    feed_currency = power_summary_value(data['feedIn']['sumCurrency']).strip()

    return {
        "consumption_sum": consumption_sum,
        "consumption_currency": consumption_currency,
        "feed_sum": feed_sum,
        "feed_currency": feed_currency
    }

import requests
from requests.auth import HTTPBasicAuth
from math import ceil, floor
from helpers.config_env import config_env
from helpers.get_date import past_date


def power_summary_value(value):
    value_1 = round(value, 2)
    value_2 = int(value*1000)/1000
    result = round((value_2-value_1)*1000)
    if result == 5:
        value = ceil(value*100)/100
    else:
        value = round(value, 2)
    return f"{value: .2f}".strip()

def prosumer_analytics(login, password):
    timestamp = int(past_date().get('timestamp'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "reportType": "dailyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/consumption"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Consumption values
    consumption_sum = power_summary_value(data['consumption']['sum'])
    feedIn_sum = power_summary_value(data['feedIn']['sum'])

    return {
        "consumption_sum": consumption_sum.replace('.', ','),
        "feedIn_sum": feedIn_sum.replace('.', ',')
    }


def generator_analytics(login, password):
    timestamp = int(past_date().get('timestamp'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-GENERATE-LEMBERG",
        "reportType": "dailyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/consumption"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Consumption values
    generation_sum = power_summary_value(data['generation']['sum'])

    return {
        "generation_sum": generation_sum.replace('.', ',')
    }


def power_group_analytics(login, password):
    timestamp = int(past_date().get('timestamp'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "division": 0,
        "mainDevice": True,
        "reportType": "dailyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/consumption"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Consumption values
    consumption_sum = power_summary_value(data['consumption']['sum'])
    own_consumption_sum = power_summary_value(data['ownConsumption']['sum'])
    total_consumption_sum = str(round((float(consumption_sum) + float(own_consumption_sum)), 2))

    return {
        "consumption_sum": consumption_sum.replace('.', ','),
        "own_consumption_sum": own_consumption_sum.replace('.', ','),
        "total_consumption_sum": total_consumption_sum.replace('.', ',')
    }

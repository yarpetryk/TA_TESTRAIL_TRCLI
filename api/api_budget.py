import requests
from requests.auth import HTTPBasicAuth
from math import ceil
from datetime import datetime
from calendar import monthrange
from helpers.config_env import config_env
from helpers.get_date import get_month


def get_value(value):
    value_1 = round(value, 2)
    value_2 = int(value*1000)/1000
    result = round((value_2-value_1)*1000)
    if result == 5:
        value = ceil(value*100)/100
    else:
        value = round(value, 2)
    return f"{value: .2f}".strip()


def get_prepayment_current_month(login, password):

    # Get days in current month
    current_day = int(datetime.now().strftime("%-d"))
    m = str(datetime.now().strftime("%-m %Y"))
    month = monthrange(int(m.split()[1]), int(m.split()[0]))[1]

    timestamp = int(get_month().get('timestamp_current_month'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "reportType": "monthlyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/budget"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Prepayment value
    value = float(get_value(data['payments'][0]))
    prepayment = f"{((value/month)*current_day): .2f}"

    return {
        "prepayment": prepayment.replace(".", ",")
    }


def get_prepayment_prev_month(login, password):
    timestamp = int(get_month().get('timestamp_prev_month'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "reportType": "monthlyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/budget"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Prepayment value
    prepayment = get_value(data['payments'][0])

    return {
        "prepayment": prepayment.replace(".", ",")
    }


def get_consumption_current_month(login, password):
    timestamp = int(get_month().get('timestamp_current_month'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "reportType": "monthlyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/consumption"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Prepayment value
    consumption_currency = get_value(data['consumption']['sumCurrency'])

    return {
        "consumption": consumption_currency.replace(".", ",")
    }


def get_consumption_prev_month(login, password):
    timestamp = int(get_month().get('timestamp_prev_month'))
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)
    body = {
        "deviceId": "POWERBOX-SYNC-LEMBERG-PROSUMER",
        "reportType": "monthlyValues",
        "startTime": timestamp
    }
    url = f"{base_url}/report/0/consumption"
    res = requests.post(url=url, auth=auth, json=body)
    data = res.json()

    # Prepayment value
    consumption_currency = get_value(data['consumption']['sumCurrency'])

    return {
        "consumption": consumption_currency.replace(".", ",")
    }

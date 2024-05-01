import requests
from requests.auth import HTTPBasicAuth
from helpers.config_env import config_env


def validate_profile(login, password):
    base_url = config_env().get('base_url')
    auth = HTTPBasicAuth(login, password)

    def get_user_info():
        url = f"{base_url}/customers/0"
        res = requests.get(url=url, auth=auth)
        data = res.json()
        return data

    user_info = get_user_info()
    user_id = user_info['customerId']
    user_info['emailAddressVerified'] = True
    url = f"{base_url}/customers/{user_id}/update"
    requests.put(url=url, auth=auth, json=user_info)



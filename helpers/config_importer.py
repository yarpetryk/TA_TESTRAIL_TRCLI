import json


class ConfigImporter:
    CONFIG_PATH = "./tests/config.json"
    DEFAULT_WAIT_TIME = 10

    def __init__(self):
        self.data = None

    def config(self):
        with open(self.CONFIG_PATH, 'r') as config_file:
            self.data = json.load(config_file)
        return self.data

    def config_username_incorrect(self):
        # Validate and return the Incorrect username from the config data
        config = self.config()
        if 'username_incorrect' not in config:
            raise Exception('The config file does not contain "username_incorrect"')
        return config['username_incorrect']

    def config_username_invalid(self):
        # Validate and return the Invalid username from the config data
        config = self.config()
        if 'username_invalid' not in config:
            raise Exception('The config file does not contain "username_invalid"')
        return config['username_invalid']

    def config_user_password_invalid(self):
        # Validate and return the Invalid user password from the config data
        config = self.config()
        if 'user_password_invalid' not in config:
            raise Exception('The config file does not contain "user_password_invalid"')
        return config['user_password_invalid']

    def config_user_password_no_match(self):
        # Validate and return the User password no matchfrom the config data
        config = self.config()
        if 'user_password_no_match' not in config:
            raise Exception('The config file does not contain "user_password_no_match"')
        return config['user_password_no_match']

    def config_user_password_short(self):
        # Validate and return the short user password from the config data
        config = self.config()
        if 'user_password_short' not in config:
            raise Exception('The config file does not contain "user_password_short"')
        return config['user_password_short']

    def config_package_name(self):
        # Validate and return the Package Name from the config data
        config = self.config()
        if 'package_name' not in config:
            raise Exception('The config file does not contain "package_name"')
        return config['package_name']

    def config_env(self):
        # Validate and return the Config env from the config data
        config = self.config()
        if 'config_env_file' not in config:
            raise Exception('The config file does not contain "config_env_file"')
        return config['config_env_file']

    def config_locale(self):
        # Validate and return the Locale from the config data
        config = self.config()
        if 'locale' not in config:
            raise Exception('The config file does not contain "locale"')
        return config['locale']

    def config_language(self):
        # Validate and return the Language from the config data
        config = self.config()
        if 'language' not in config:
            raise Exception('The config file does not contain "language"')
        return config['language']

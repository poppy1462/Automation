from configparser import ConfigParser


class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait time option is not present in the config file")
        return int(value)

    def get_email(self):
        value = self.data.get('user1', 'email', fallback=None)
        if value is None:
            raise Exception("Email option is not present in the config file")
        return value

    def get_password(self):
        value = self.data.get('user1', 'password', fallback=None)
        if value is None:
            raise Exception("Password option is not present in the config file")
        return value

    def get_screen_width(self):
        value = self.data.get('environment', 'screen_width', fallback=None)
        if value is None:
            raise Exception("Screen width option is not present in the config file")
        return int(value)

    def get_screen_height(self):
        value = self.data.get('environment', 'screen_height', fallback=None)
        if value is None:
            raise Exception("Screen height option is not present in the config file")
        return int(value)

    def get_user1_email(self):
        value = self.data.get('user1', "email", fallback=None)
        if value is None:
            raise Exception("email option is not found in user1 section")
        return value

    def get_user1_password(self):
        value = self.data.get('user1', "password", fallback=None)
        if value is None:
            raise Exception("password option is not found in user1 section")
        return value

    def get_user1_first_name(self):
        value = self.data.get('user1', "first_name", fallback=None)
        if value is None:
            raise Exception("first_name option is not found in user1 section")
        return value

    def get_user1_last_name(self):
        value = self.data.get('user1', "last_name", fallback=None)
        if value is None:
            raise Exception("last_name option is not found in user1 section")
        return value

    def get_user1_telephone(self):
        value = self.data.get('user1', "telephone", fallback=None)
        if value is None:
            raise Exception("telephone option is not found in user1 section")
        return value

    def get_user1_address(self):
        value = self.data.get('user1', "address", fallback=None)
        if value is None:
            raise Exception("address option is not found in user1 section")
        return value

    def get_user1_city(self):
        value = self.data.get('user1', "city", fallback=None)
        if value is None:
            raise Exception("city option is not found in user1 section")
        return value

    def get_user1_country(self):
        value = self.data.get('user1', "country", fallback=None)
        if value is None:
            raise Exception("country option is not found in user1 section")
        return value

    def get_user1_state(self):
        value = self.data.get('user1', "state", fallback=None)
        if value is None:
            raise Exception("state option is not found in user1 section")
        return value

    def get_user2_email(self):
        value = self.data.get('user2', "email", fallback=None)
        if value is None:
            raise Exception("email option is not found in user2 section")
        return value

    def get_user2_password(self):
        value = self.data.get('user2', "password", fallback=None)
        if value is None:
            raise Exception("password option is not found in user2 section")
        return value

    def get_user2_first_name(self):
        value = self.data.get('user2', "first_name", fallback=None)
        if value is None:
            raise Exception("first_name option is not found in user2 section")
        return value

    def get_user2_last_name(self):
        value = self.data.get('user2', "last_name", fallback=None)
        if value is None:
            raise Exception("last_name option is not found in user2 section")
        return value

    def get_user2_telephone(self):
        value = self.data.get('user2', "telephone", fallback=None)
        if value is None:
            raise Exception("telephone option is not found in user2 section")
        return value

    def get_user2_address(self):
        value = self.data.get('user2', "address", fallback=None)
        if value is None:
            raise Exception("address option is not found in user2 section")
        return value

    def get_user2_city(self):
        value = self.data.get('user2', "city", fallback=None)
        if value is None:
            raise Exception("city option is not found in user2 section")
        return value

    def get_user2_country(self):
        value = self.data.get('user2', "country", fallback=None)
        if value is None:
            raise Exception("country option is not found in user2 section")
        return value

    def get_user2_state(self):
        value = self.data.get('user2', "state", fallback=None)
        if value is None:
            raise Exception("state option is not found in user2 section")
        return value




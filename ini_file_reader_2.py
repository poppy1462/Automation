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


import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_email(self):
        if 'email' not in self.data.keys():
            raise Exception("Email option is not present in the config file")
        return self.data['email']

    def get_password(self):
        if 'password' not in self.data.keys():
            raise Exception("Password option is not present in the config file")
        return self.data['password']

    def get_screen_width(self):
        if 'screen_width' not in self.data.keys():
            raise Exception("Screen width option is not present in the config file")
        return int(self.data['screen_width'])

    def get_screen_height(self):
        if 'screen_height' not in self.data.keys():
            raise Exception("Screen height option is not present in the config file")
        return int(self.data['screen_height'])
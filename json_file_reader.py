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
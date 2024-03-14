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

    def get_user1_email(self):
        if 'email' not in self.data.keys():
            raise Exception("email option is not found in user1 section")
        return self.data['email']

    def get_user1_password(self):
        if 'password' not in self.data.keys():
            raise Exception("password option is not found in user1 section")
        return self.data['password']

    def get_user1_first_name(self):
        if 'first_name' not in self.data.keys():
            raise Exception("first_name option is not found in user1 section")
        return self.data['first_name']

    def get_user1_last_name(self):
        if 'last_name' not in self.data.keys():
            raise Exception("last_name option is not found in user1 section")
        return self.data['last_name']

    def get_user1_telephone(self):
        if 'telephone' not in self.data.keys():
            raise Exception("telephone option is not found in user1 section")
        return self.data['telephone']

    def get_user1_address(self):
        if 'address' not in self.data.keys():
            raise Exception("address option is not found in user1 section")
        return self.data['address']

    def get_user1_city(self):
        if 'city' not in self.data.keys():
            raise Exception("city option is not found in user1 section")
        return self.data['city']

    def get_user1_county(self):
        if 'county' not in self.data.keys():
            raise Exception("county option is not found in user1 section")
        return self.data['county']

    def get_user1_state(self):
        if 'state' not in self.data.keys():
            raise Exception("state option is not found in user1 section")
        return self.data['state']

    def get_user2_email(self):
        if 'email2' not in self.data.keys():
            raise Exception("email option is not found in user2 section")
        return self.data['email2']

    def get_user2_password(self):
        if 'password2' not in self.data.keys():
            raise Exception("password option is not found in user2 section")
        return self.data['password2']

    def get_user2_first_name(self):
        if 'first_name2' not in self.data.keys():
            raise Exception("first_name option is not found in user2 section")
        return self.data['first_name2']

    def get_user2_last_name(self):
        if 'last_name2' not in self.data.keys():
            raise Exception("last_name option is not found in user2 section")
        return self.data['last_name2']

    def get_user2_telephone(self):
        if 'telephone2' not in self.data.keys():
            raise Exception("telephone option is not found in user2 section")
        return self.data['telephone2']

    def get_user2_address(self):
        if 'address2' not in self.data.keys():
            raise Exception("address option is not found in user2 section")
        return self.data['address2']

    def get_user2_city(self):
        if 'city2' not in self.data.keys():
            raise Exception("city option is not found in user2 section")
        return self.data['city2']

    def get_user2_county(self):
        if 'county2' not in self.data.keys():
            raise Exception("county option is not found in user12 section")
        return self.data['county2']

    def get_user2_state(self):
        if 'state2' not in self.data.keys():
            raise Exception("state option is not found in user2 section")
        return self.data['state2']
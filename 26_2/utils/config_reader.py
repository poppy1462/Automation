from BrainBucketTesting.utils.json_file_reader import JsonFileReader
from BrainBucketTesting.utils.ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_url(self):
        return self.reader.get_url()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    def get_email(self):
        return self.reader.get_email()

    def get_password(self):
        return self.reader.get_password()

    def get_screen_width(self):
        return self.reader.get_screen_width()

    def get_screen_height(self):
        return self.reader.get_screen_height()

    def get_user1_email(self):
        return self.reader.get_user1_email()

    def get_user1_password(self):
        return self.reader.get_user1_password()

    def get_user1_first_name(self):
        return self.reader.get_user1_first_name()

    def get_user1_last_name(self):
        return self.reader.get_user1_last_name()

    def get_user1_telephone(self):
        return self.reader.get_user1_telephone()

    def get_user1_address(self):
        return self.reader.get_user1_address()

    def get_user1_city(self):
        return self.reader.get_user1_city()

    def get_user1_country(self):
        return self.reader.get_user1_country()

    def get_user1_state(self):
        return self.reader.get_user1_state()

    def get_user2_email(self):
        return self.reader.get_user2_email()

    def get_user2_password(self):
        return self.reader.get_user2_password()

    def get_user2_first_name(self):
        return self.reader.get_user2_first_name()

    def get_user2_last_name(self):
        return self.reader.get_user2_last_name()

    def get_user2_telephone(self):
        return self.reader.get_user2_telephone()

    def get_user2_address(self):
        return self.reader.get_user2_address()

    def get_user2_city(self):
        return self.reader.get_user2_city()

    def get_user2_country(self):
        return self.reader.get_user2_country()

    def get_user2_state(self):
        return self.reader.get_user2_state()



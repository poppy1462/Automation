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




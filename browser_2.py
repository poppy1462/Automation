from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from datetime import datetime

class Browser:
    """
    This class is wrapper around Selenium driver
    """

    def __init__(self, url, browser_name="", time_wait = 10, screen_height=None, screen_width=None):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            try:
                options = webdriver.FirefoxOptions()
                options.add_argument("--width=600") #to open in mobile size screen
                options.add_argument("--height=800")
                #options.add_argument("--disable-extensions") - to disable extensions

                # firefox_profile = webdriver.FirefoxProfile()- to disable popup blocking
                # firefox_profile.set_preference("browser.urlbar.showPopup", True)
                # self.driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path='drivers/geckodriver', options=options)

                #firefox_profile = webdriver.FirefoxProfile()- to open in incognito window
                #firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
                #self.driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path='drivers/geckodriver', options=options)

                self.driver = webdriver.Firefox(executable_path='drivers/geckodriver', options=options)
                self.driver.maximize_window()
            except WebDriverException:
                print("The executable path to the driver is incorrect")

        else:
            try:
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized") #to open in full-size screen
                if screen_width is not None and screen_height is not None:
                    options.add_argument(f"--window-size={screen_width},{screen_height}") #to open in mobile screen size
                #options.add_argument("--incognito") - to open in incognito window
                #options.add_argument("--disable-extensions") - to disable extensions
                #options.add_argument("--disable-popup-blocking") - to disable blocking pop-up windows
                options.add_experimental_option("excludeSwitches", ['enable-automation']) #to prevent displaying "Chrome is being controlled by automated software" message
                self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver', options=options)
            except WebDriverException:
                print("The executable path to the driver is incorrect")

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()



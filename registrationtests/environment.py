from BrainBucketTesting.utils.config_reader import ConfigReader
from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.pages.registration_page import RegistrationPage


def before_all(context):
    configs = ConfigReader("/Users/anastasiatskhay/PycharmProjects/PythonIntro/BrainBucketTesting/BDDBehave/registrationtests/steps/config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
    context.browser = browser
    registration_page = RegistrationPage(context.browser)
    context.registration_page = registration_page


def after_scenario(context, scenario):
    print("The scenario was tested")
    browser = context.browser
    browser.shutdown()

def after_all(context):
    print("All tests are completed")


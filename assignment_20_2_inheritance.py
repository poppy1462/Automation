from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from BrainBucketTesting.webelements.dropdown import Dropdown
from BrainBucketTesting.webelements.radiobutton import Radiobutton
from BrainBucketTesting.webelements.radiobutton import Checkbox


browser = Browser("https://cleveronly.com/brainbucket")
driver = browser.get_driver()

#in Account dropdown select Register option
account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
account_btn.click()

# wait till DropDown will open
Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible()

#select Register option
Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]").click()

registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
assert registration_form_title.get_text() == 'Register Account'

inputs = {
    'firstname': "Anastasia",
    'lastname': "Tskhay",
    'email': "test@gmail.com",
    'telephone': "1234567890",
    'fax': "0987654321",
    'company': "Test Company",
    'address_1': "575 W Madison St",
    'city': "Chicago",
    'password': "qwerty123",
    'confirm': "qwerty123"
}

for field, text in inputs.items():
    input_field = Element(browser, By.NAME, field)
    input_field.enter_text(text)

#find dropdown element for Country
Dropdown(browser, By.ID, 'input-country').select_by_text("United States")

#find dropdown element for Region
Dropdown(browser, By.NAME, 'zone_id').select_by_text("Illinois")

#clicking on subscribe YES radio button
Radiobutton(browser, By.XPATH, "//input[@name='newsletter' and @value='1']").select_if_not_selected()

#agreeing to Policy
Checkbox(browser, By.NAME, "agree").select_if_not_selected()


Element(browser, By.XPATH, "//input[@value='Continue']").submit()

successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

time.sleep(5)
browser.shutdown()
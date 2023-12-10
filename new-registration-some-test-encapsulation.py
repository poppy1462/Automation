from selenium import webdriver
from selenium.webdriver.support.color import Color

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#import Select module
from selenium.webdriver.support.select import Select

#import encapsulation scripts
from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element


#opening Chrome browser and opening the Brain Bucket URL
browser = Browser("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver = browser.get_driver()


#verifying the logo is present. If it can't return the web element, it will return an error. Otherwise we won't see anything visually.
Element(browser, By.XPATH, "//img[@title='Brainbucket']").wait_until_visible()

#Clicking the Continue button
Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]").click()

#getting the background color of the button
#background_color = new_registrant_btn.value_of_css_property("background-color")
#converted_background_color = Color.from_string(background_color)
#assert converted_background_color.rgb == 'rgb(34, 154, 200)'


#checking the Register Account Title
registration_form_title = Element(browser, By.XPATH, "//h1[contains(text(), 'Register Account')]")
assert registration_form_title.get_text() == 'Register Account'

#Entering Personal Details

#FirstName
firstname_field = Element(browser, By.XPATH, "//fieldset/div[2]")
assert "required" in firstname_field.get_attribute("class")
Element(browser, By.ID, "input-firstname").enter_text('Anastasia')


#LastName
lastname_field = Element(browser, By.XPATH, "//fieldset/div[3]")
assert "required" in lastname_field.get_attribute("class")
Element(browser, By.ID, "input-lastname").enter_text('Tskhay')


#Email
email_field = Element(browser, By.XPATH, "//fieldset/div[4]")
assert "required" in email_field.get_attribute("class")
Element(browser, By.ID, "input-email").enter_text('test@test.com')


#Telephone
telephone_field = Element(browser, By.XPATH, "//fieldset/div[5]")
assert "required" in telephone_field.get_attribute("class")
Element(browser, By.ID, "input-telephone").enter_text('111-222-3333')


#Fax
fax_field = Element(browser, By.XPATH, "//fieldset/div[6]")
assert "required" not in fax_field.get_attribute("class")
Element(browser, By.ID, "input-fax").enter_text('222-333-4444')


#Company
company_field = Element(browser, By.XPATH, "//fieldset[2]/div[1]")
assert "required" not in company_field.get_attribute("class")
Element(browser, By.ID, "input-company").enter_text('Test Company')


#Address 1
address1_field = Element(browser, By.XPATH, "//fieldset[2]/div[2]")
assert "required" in address1_field.get_attribute("class")
Element(browser, By.ID, "input-address-1").enter_text('575 W Madison St')


#Address 2
address2_field = Element(browser, By.XPATH, "//fieldset[2]/div[3]")
assert "required" not in address2_field.get_attribute("class")
Element(browser, By.ID, "input-address-2").enter_text('Apt 4304')


#City
city_field = Element(browser, By.XPATH, "//fieldset[2]/div[4]")
assert "required" in city_field.get_attribute("class")
Element(browser, By.ID, "input-city").enter_text('Chicago')


#Post Code
postcode_field = Element(browser, By.XPATH, "//fieldset[2]/div[5]")
assert "required" not in postcode_field.get_attribute("class")
Element(browser, By.ID, "input-postcode").enter_text('60661')


#Select Country
country_dropdown = Element(browser, By.ID, "input-country").get_element()
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_visible_text("United States")

#Select Region/State
zone_dropdown = Element(browser, By.ID, "input-zone").get_element()
zone_dropdown_select = Select(zone_dropdown)
zone_dropdown_select.select_by_visible_text("Illinois")


#Password
password_field = Element(browser, By.XPATH, "//fieldset[3]/div[1]")
assert "required" in password_field.get_attribute("class")
Element(browser, By.ID, "input-password").enter_text('Qwerty123')


#Confirm Password
confirm_field = Element(browser, By.XPATH, "//fieldset[3]/div[2]")
assert "required" in confirm_field.get_attribute("class")
Element(browser, By.ID, "input-confirm").enter_text('Qwerty123')


#subscribe to newsletter
subscribe_btn = Element(browser, By.XPATH, "//input[@name='newsletter' and @value='1']").get_element()
if not subscribe_btn.is_selected():
    subscribe_btn.click()

#Privacy policy agreement
privacy_btn = Element(browser, By.XPATH, "//input[@name='agree' and @value='1']").get_element()
if not privacy_btn.is_selected():
    privacy_btn.click()

#land on the Register page in the "My Account" dropdown
Element(browser, By.XPATH, "//a[@title='My Account']").click()
Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible()
Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]").click()

#to close the browser
shutdown = browser.shutdown()
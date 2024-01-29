from selenium.webdriver.common.by import By
import time

from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from BrainBucketTesting.webelements.dropdown import Dropdown

from BrainBucketTesting.components.header import Header
from BrainBucketTesting.components.navigation_bar import NavigationBar

from BrainBucketTesting.pages.home_page import HomePage

URL = "https://cleveronly.com/brainbucket"
browser = Browser(URL)
driver = browser.get_driver()


def test_all_pcs():
    homepage = HomePage(browser)
    homepage.show_pcs()


    #pc_dropdown_xpath = homepage.navbar.desktops_dropdown.select_by_option_xpath("//a[contains(text(), 'PC')]")
    #print(pc_dropdown_xpath.get_locator())

def show_all_desktops():
    homepage = HomePage(browser)
    homepage.show_all_desktops()

def test_all_macs():
    homepage = HomePage(browser)
    homepage.show_mac_laptops()

def test_mac_desktops():
    homepage = HomePage(browser)
    homepage.show_mac_desktops()
    number_of_macs = homepage.get_number_of_macs_from_dropdown()
    number_of_displayed_products = homepage.get_number_of_products()
    assert number_of_macs == number_of_displayed_products

def test_windows_laptops():
    homepage = HomePage(browser)
    homepage.show_windows_laptops()
    message_text = homepage.get_no_products_message()
    assert message_text == "There are no products to list in this category."


def test_printers():
    homepage = HomePage(browser)
    homepage.show_printers()

def test_pdas():
    homepage = HomePage(browser)
    homepage.show_pdas()



if __name__ == "__main__":
    #test_all_pcs()
    #show_all_desktops()
    #test_all_macs()
    #test_mac_desktops()
    #test_printers()
    test_mac_desktops()
    test_windows_laptops()

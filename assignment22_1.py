from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time

from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.actions import Actions
from BrainBucketTesting.webelements.UIElement import UIElement as Element

URL = "https://cleveronly.com/practice/"
browser = Browser(URL)
driver = browser.get_driver()




# Part1: Double click (verify that the background color is changed after performing double click)

card = Element(browser, By.ID, 'card')
card.verify_color(color='rgb(255, 238, 153)')
dbl_click = Actions(browser)
dbl_click.double_click(element=card)
card.verify_color(color='rgb(255, 179, 128)')




# Part2: Press enter in the input field (verify that the message "You pressed the key!" is displayed after you perform the action)

keydown = Element(browser, By.XPATH, '//input[@type="text"]')

press_enter = Actions(browser)
press_enter.send_keys_to_element(element=keydown, keys_to_send='\ue007')

pressed_key_message = Element(browser, By.ID, 'hidden_text')
assert pressed_key_message.get_text() == 'You pressed the key!'



# Part3: Open Context menu and select all available options from it

banner = Element(browser, By.ID, 'context_menu')
open_context_menu = Actions(browser)
open_context_menu.right_click(element=banner)

# Change color (verify that the background color is changed for the box)

banner.verify_color(color='rgba(204, 204, 255, 0.8)', a=True)
color_btn = Element(browser, By.XPATH, '//*[text()="Change Color"]')
change_color = Actions(browser)
change_color.click(element=color_btn)
banner.verify_color(color='rgb(204, 255, 245)')

# Change font (verify that the text in the box becomes bold after it)

open_context_menu.right_click(element=banner)
font_btn = Element(browser, By.XPATH, '//*[text()="Change Font"]')
change_font = Actions(browser)
change_font.click(element=font_btn)
banner.verify_font()

# Open CleverOnly

open_context_menu.right_click(element=banner)
link_btn = Element(browser, By.XPATH, '//*[text()="Open TechSkillAcademy"]')
click_link = Actions(browser)
click_link.click(element=link_btn)

# Closing Context Menu by sending ESC Key to the page

close_menu = Actions(browser)
close_menu.send_keys(keys_to_send='\ue00c')



# Part4: Drag the drop the logo

logo = Element(browser, By.ID, 'drag1')
frame = Element(browser, By.ID, 'droplogo123')
drag_logo = Actions(browser)
drag_logo.drag_and_drop(source=logo, target=frame)





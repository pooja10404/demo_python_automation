from src.common import webdriver_utility

deal_header = 'deals'
menu_item = '//h5[contains(text(),\'item_name\')]'


# This function is for wait till "Deal" header is not present on the page.
def wait_for_menu_page_to_load():
    webdriver_utility.wait_for_element_visible('ID', deal_header)


# Clicks on the item for product detils page.
def click_item(item_name):
    webdriver_utility.click('XPATH', menu_item.replace('item_name', item_name))

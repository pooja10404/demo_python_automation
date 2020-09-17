from src.common import base_test
from src.common import webdriver_utility

# Locators / Elements on the order page
enter_your_address_textbox = 'addresstext'
address_search_listing_first_value = 'div.tt-dataset.tt-dataset-2'
delivery_for_store = '//h5[@class="card-title" and text()=\'store_name\']/..//button[contains' \
                     '(@class,\'btn-store-delivery\')]/..'
continue_button_confirm_address = 'address-confirmation-modal-continue-btn'
loading_select_delivery_time = 'option[value=\'LOADING\']'
delivery_date_picker = "delivery-datepicker"
next_button_date_picker = "a[data-handler=\"next\"]"
date_date_picker = "//a[text()='1']"
continue_button_delivery = 'button.btn-datetime-submit'


# Function for search the address
# @param : address: address to type in the search textbox.
def search_address(address):
    webdriver_utility.enter_value('ID', enter_your_address_textbox, address)
    webdriver_utility.click('CSS', address_search_listing_first_value)


# Function for click on store for delivery
# @param : store: Name of the store for delivery.
def click_delivery_for_store(store):
    webdriver_utility.click('XPATH', delivery_for_store.replace('store_name', store))


# Function for click on continue button on the confirm address popup.
def click_continue_confirm_address_popup():
    webdriver_utility.click('ID', continue_button_confirm_address)


# Function for select the first date from the calender and click on continue button.
def select_delivery_time_and_continue():
    webdriver_utility.wait_for_element_invisible('CSS', loading_select_delivery_time)
    webdriver_utility.click('ID', delivery_date_picker)
    webdriver_utility.click('CSS', next_button_date_picker)
    webdriver_utility.click('XPATH', date_date_picker)
    webdriver_utility.wait_for_element_invisible('CSS', loading_select_delivery_time)
    webdriver_utility.click('CSS', continue_button_delivery)


# This function it to navigate to the order page.
def navigate_to_order():
    base_test.get_driver().get(base_test.configs.get('Url').data + "/order")

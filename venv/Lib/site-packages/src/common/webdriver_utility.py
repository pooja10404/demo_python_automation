from selenium.webdriver.common.by import By

from src.common import base_test
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Find element on page
# @param : locator_strategy : can be the XPATH, ID, CSS for now
# @param : locator : locator for the element.
# @returns : element
def find_element(locator_strategy, locator):
    element = ''
    if locator_strategy == 'ID':
        element = WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.ID, locator)))
    if locator_strategy == 'XPATH':
        element = WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
    if locator_strategy == 'CSS':
        element = WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    return element


# Types/enter value in the textbox.
def enter_value(locator_strategy, locator, value):
    find_element(locator_strategy, locator).send_keys(value)


# Clicks on the element
def click(locator_strategy, locator):
    find_element(locator_strategy, locator).click()


# Returns the text of the element
def get_text(locator_strategy, locator):
    return find_element(locator_strategy, locator).text


# wait till the element is invisible on the page.
def wait_for_element_invisible(locator_strategy, locator):
    if locator_strategy == 'ID':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.invisibility_of_element((By.ID, locator)))
    if locator_strategy == 'XPATH':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.invisibility_of_element((By.XPATH, locator)))
    if locator_strategy == 'CSS':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, locator)))


# Waits till element is visible on the page.
def wait_for_element_visible(locator_strategy, locator):
    if locator_strategy == 'ID':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.ID, locator)))
    if locator_strategy == 'XPATH':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
    if locator_strategy == 'CSS':
        WebDriverWait(base_test.get_driver(), 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

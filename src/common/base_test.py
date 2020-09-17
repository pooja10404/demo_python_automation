from selenium import webdriver
import pytest
from jproperties import Properties

configs = Properties()
driver = webdriver.Chrome(
    executable_path="./resources/driver/windows/chrome/chromedriver.exe")


def setup_module():
    driver.maximize_window()
    with open('./input/application.properties', 'rb') as config_file:
        configs.load(config_file)
    driver.get(configs.get('Url').data)


def teardown_module():
    driver.close()


def get_driver():
    return driver

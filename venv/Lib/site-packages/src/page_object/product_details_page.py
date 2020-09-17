from src.common import webdriver_utility

product_description = '//p[contains(text(),\'desc\')]'


# Verification of the presence of item description.
def verify_description_should_be_present(description):
    text = webdriver_utility.get_text('XPATH', product_description.replace('desc', description))
    assert text == description

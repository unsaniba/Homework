from behave import given, when, then
from selenium.webdriver.common.by import By


URL = 'https://www.amazon.com/Lamicall-Cell-Phone-Stand-Dock/dp/B01HPI5AM2?ref_=Oct_DLandingS_D_19c7affc_3'
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')


@given('Open Amazon Product page')
def open_amazon(context):
    context.driver.get(URL)


@when('Click on add to Cart')
def click_on_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@then('Verify the item is added to Cart')
def verify_item_add_to_cart(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(*CART_SUCCESS_MESSAGE).text
    assert expected_result == actual_result, f'Error, expected {expected_result} not found in actual {actual_result}'

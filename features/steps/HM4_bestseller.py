from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


BESTSELLER_LINK = (By.CSS_SELECTOR, 'a[href*="nav_cs_bestsellers"]')
BESTSELLER_5_LINKS = (By.CSS_SELECTOR, 'a[href*="ref=zg_bs_tab"]')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click BESTSELLER')
def click_on_bestseller(context):
    # context.driver.find_element(*BESTSELLER_LINK).click()
    context.driver.wait.until(EC.element_to_be_clickable(BESTSELLER_LINK)).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLER_5_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} Links but got {len(links)}'

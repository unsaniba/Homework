from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://www.amazon.com/gp/help/customer/display.html'
HELP_TITLE = (By.CSS_SELECTOR, '.fs-heading.bolded')
CARD_CONTAINER = (By.CSS_SELECTOR, '.issue-card-container')
SEARCH_BOX = (By.ID, 'hubHelpSearchInput')
HELP_TOPICS = (By.CSS_SELECTOR, '.help-topics-list-wrapper')


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get(URL)


@then('Verify Help Page has Card Container')
def verify_card_container(context):
    context.driver.find_element(*CARD_CONTAINER)


@then('Verify Help Page has Search Box')
def verify_search_box(context):
    context.driver.find_element(*SEARCH_BOX)


@then('Verify Help Page has help topics')
def verify_help_topics(context):
    context.driver.find_element(*HELP_TOPICS)


@then('Verify Help Page has {expected_amount} h2 Title')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HELP_TITLE)
    assert len(links) == expected_amount, f'Expected {expected_amount} Links but got {len(links)}'


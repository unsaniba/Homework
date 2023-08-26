from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.amazon.com/gp/product/B08JHKQPBV/'
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open AM Product page')
def open_amazon(context):
    context.driver.get(URL)


@then('Verify User can Click Through Color')
def verify_cam_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue']
    actual_colors = []

    colors = context.driver.find_element(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)
        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

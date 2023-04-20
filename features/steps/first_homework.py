from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

GIVEN_WEBSITE = 'http://suninjuly.github.io/xpath_examples'
FIND = ''


@given('Navigate to Xpath_Examples website')
def open_google(context):
    context.driver.get(GIVEN_WEBSITE)


@when("Locate {selector} with given {x_c}")
def input_search(context, selector, x_c):
    global FIND
    if x_c == 'x':
        FIND = context.driver.find_element(By.XPATH, selector)
    else:
        FIND = context.driver.find_element(By.CSS_SELECTOR, selector)


@then('Verify {search_item} is in there')
def click_search_icon(context, search_item):
    global FIND
    print(FIND.text)
    assert FIND.text == search_item, f"The text is {FIND.text}"



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'

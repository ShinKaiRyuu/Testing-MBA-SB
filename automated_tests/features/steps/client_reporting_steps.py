from behave import *
from nose.tools import assert_in, assert_not_equal, assert_equal, assert_true
from selenium.common.exceptions import UnexpectedAlertPresentException

use_step_matcher("re")


@step("I click Search for Client Information")
def step_impl(context):
    context.page.search_btn_click()


@then("I want to see filtered data")
def step_impl(context):
    data = context.page.get_data(column=context.filter_type)
    for d in data:
        assert_in(normalize_value(context.filter_value), d)


def normalize_value(value):
    values_map = {
        'Hourly': 'Hour'
    }
    return values_map[value]


@when("I click to (?P<page>.+)")
def step_impl(context, page):
    data = context.page.get_all_page_data()
    if not hasattr(context, 'old_page_data'):
        context.old_page_data = data
    context.page_data = data
    if page.lower() == 'next':
        context.page.to_next_page()
    elif page.lower() == 'previous':
        context.page.to_previous_page()
    else:
        raise Exception('Unknown page')


@then("I want to see (?P<data>.+) values")
def step_impl(context, data):
    if data == 'new':
        assert_not_equal(context.page_data, context.page.get_all_page_data())
    elif data == 'previous':
        assert_equal(context.old_page_data, context.page.get_all_page_data())
    else:
        raise Exception('Unknown data')


@step("data paginated")
def step_impl(context):
    context.page.set_date_and_search()


@when("I click on client row")
def step_impl(context):
    success = False
    while not success:
        try:
            context.page.random_client_row_click()
            success = True
        except UnexpectedAlertPresentException:
            alert = context.driver.switch_to_alert()
            alert.accept()


@then("I want to see client information")
def step_impl(context):
    assert_true(context.page.is_element_present('client_info'))

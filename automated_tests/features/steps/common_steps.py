from ast import literal_eval
from behave import *
from nose.tools import assert_in, assert_equal, assert_true
from helpers.shopify_helpers import get_shopify_orders

use_step_matcher("re")


@then("I want to get result - (?P<result>.+)")
def step_impl(context, result):
    context.execute_steps("""
        Then {}
    """.format(result))


@step("I click Submit Form button")
def step_impl(context):
    context.page.submit()


@step("I want to see success message")
def step_impl(context):
    assert_equal(context.page.success_message, context.page.s_message_element.text)


@step('I want to see error message "(?P<message>.+)"')
def step_impl(context, message):
    import time

    time.sleep(1)

    error_messages = list(filter(bool, context.page.get_error_messages()))
    assert_in(message.strip(), error_messages)
    assert_true(0 < len(error_messages) <= 2, error_messages)


@given("I have (?P<product>.+) in cart")
def step_impl(context, product):
    product = literal_eval(product)
    context.execute_steps('''
        Given I am on {type} page
        When I choose {item_name} item
        And I adding this service to cart
    '''.format(**product))


@then("I want to see that I am logged out")
def step_impl(context):
    assert_true(context.page.is_element_present('to_login_form_btn'))


@when("I choose option (?P<option>.+) of select (?P<select>.+)")
def step_impl(context, option, select):
    context.filter_type = select
    context.filter_value = option
    context.page.choose_option_of_select(option, select)


@step("I click (?P<btn_text_or_title>.+) button")
def step_impl(context, btn_text_or_title):
    if hasattr(context.page, 'save_table'):
        context.page.save_table()

    if 'on table' in context.step_name:
        context.page.click_btn_by_title(btn_text_or_title)
    elif 'on widget' in context.step_name:
        context.page.click_by_text(btn_text_or_title)
    else:
        context.page.click_btn_by_text(btn_text_or_title)


@then('I want to see message "(?P<message>.+)"')
def step_impl(context, message):
    assert_equal(message, context.page.get_message())


@step("I reloading page")
def step_impl(context):
    context.driver.refresh()
    context.page.wait_for_loading(240)


@step('fail')
@step('Fail')
def step_impl(context):
    raise NotImplementedError


@step("I have new transaction")
def step_impl(context):
    last_order = next(iter(get_shopify_orders(orders_number=1)))
    context.expected_row = {
        'first_name': last_order['customer']['name'].split()[0],
        'last_name': last_order['customer']['name'].split()[-1],
        'email': last_order['customer']['email'],
        'fiscal_year': last_order['date']['fiscal_year'],
        'service': last_order['order']['product'],
        'amount': last_order['total']
    }
    # print('exp -', context.expected_row)
    assert_equal(context.expected_row['email'], context.customer_information['email'])


@then("I want to see new transaction")
def step_impl(context):
    row_data = None
    context.added_row = getattr(context, 'added_row', None)
    attempts = 5 if not context.added_row else 1
    while attempts:
        try:
            context.page.wait_for_loading(seconds=360)
            row_data = context.page.get_row_data()
            # print('row_data -', row_data)
            _check_transaction(context, row_data)
            context.added_row = True
            break
        except AssertionError:
            context.page.open()
            attempts -= 1
    else:
        _check_transaction(context, row_data)


def _check_transaction(context, row_data):
    if context.page_name == 'Manage Billing':
        assert_equal(context.expected_row, row_data)
    elif context.page_name in ['Billing Reporting', 'Consultant Dashboard']:
        for v in context.expected_row.values():
            assert_in(v, row_data)

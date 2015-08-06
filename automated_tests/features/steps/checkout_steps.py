from behave import *
from nose.tools import assert_equal, assert_true

use_step_matcher("re")


@step("product info and price are the same")
def step_impl(context):
    assert_equal(context.page.get_product_name(), context.item_name)
    assert_equal(context.page.product_price.text, context.package['price'])


@when("I fill in Billing address form with required data")
def step_impl(context):
    customer_info = getattr(context, 'customer_information', {'f_name': '1', 'l_name': '1'})
    print(customer_info)
    context.page.fill_billing_address_form(customer_info)


@step("I click Continue to next step button")
def step_impl(context):
    context.page.to_next_step_btn.click()


@when("I fill in Payment info")
def step_impl(context):
    context.page.fill_payment_info()


@step("I click Complete my purchase button")
def step_impl(context):
    context.page.complete_btn.click()


@then("I want to see that purchase completed")
def step_impl(context):
    assert_true(context.page.purchase_completed())


@step("I complete my purchase")
def step_impl(context):
    context.execute_steps('''
        Then I click Check Out button
        Then I want to see Check Out page
        Then product info and price are the same
        When I fill in Billing address form with required data
        Then I click Continue to next step button
        Then I want to see Complete My Purchase page
        When I fill in Payment info
        Then I click Complete my purchase button
        Then I want to see that purchase completed
    ''')

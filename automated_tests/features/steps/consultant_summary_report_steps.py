from datetime import datetime
from behave import *
from nose.tools import assert_equal, assert_in

use_step_matcher("re")


@when("I click on current month link")
def step_impl(context):
    context.page.click_current_month_link()


@then("I want to see all clients for current month")
def step_impl(context):
    current_month = datetime.now().strftime("%m")
    invoice_months = set(context.page.get_invoice_months())
    assert_equal(1, len(invoice_months))
    assert_equal(current_month, list(invoice_months)[0])


@when("click on client")
def step_impl(context):
    context.client_name = context.page.click_client()


@then("I want to see all records only for that client")
def step_impl(context):
    clients = set(context.page.get_clients())
    assert_equal(1, len(clients))
    assert_equal(context.client_name, list(clients)[0])


@then("I want to see Consultant Summary Report for chosen consultant")
def step_impl(context):
    context.execute_steps('''
        Then I want to see Consultant Summary Report page
    ''')
    assert_in(context.consultant, context.driver.page_source)

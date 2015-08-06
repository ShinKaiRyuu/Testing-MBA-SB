from behave import *
from faker import Faker
from nose.tools import assert_equal, assert_in, assert_not_equal

use_step_matcher("re")


@when("I choose (?P<date_value>.+) in Date field")
def step_impl(context, date_value):
    if date_value == 'first day of current month':
        context.page.choose_first_day()


@then("I want to see information for that fiscal year up to that Date")
def step_impl(context):
    context.page.wait_for_loading()
    if context.page_name == 'Consultant Dashboard':
        assert_not_equal(context.page.consultant_billing_table_text, context.page.consultant_billing_table.text)
    elif context.page_name == 'Consultant Summary Report':
        assert_not_equal(context.page.summary_report_text, context.page.summary_report_table.text)
    elif context.page_name == 'Consultant Administrator Dashboard':
        assert_not_equal(context.page.summary_consultants_text, context.page.summary_consultants_table.text)
    else:
        raise NotImplementedError


@when("I select (?P<table_name>.+) table row")
def step_impl(context, table_name):
    context.table_name = table_name
    context.row_data = context.page.get_row_data(table_name)
    context.page.select_row(table_name)


@step("I edit (?P<field_name>.+) field with (?P<field_value>.+)")
def step_impl(context, field_name, field_value):
    context.field_name = field_name
    context.field_value = field_value
    context.page.update_field(field_name, field_value)


@then("I want to see updated row information")
def step_impl(context):
    expected_row_data = update_data(context.row_data, context.field_name, context.field_value)
    assert_equal(expected_row_data, context.page.get_row_data(context.table_name))


def update_data(data, field_name, field_value):
    d = data[:]
    fields_indexes_map = {
        'Fiscal year': 5,
        'Contract status': 7,
        'Consultant': 8,
        'Free Consultant': 9
    }
    d[fields_indexes_map[field_name]] = field_value
    return d


@when('I see client with Client Status "On"')
def step_impl(context):
    context.client_number = context.page.get_active_client_number()


@step('I click "\+" on client')
def step_impl(context):
    context.page.click_client_plus(context.client_number)


@step('I click "\+" on transaction')
def step_impl(context):
    context.page.click_transaction_plus()


@then("I want to be able to add invoice")
def step_impl(context):
    context.execute_steps('''
        When I click Add new row button on table
    ''')
    faker = Faker()
    context.invoice_data = {
        'schoolName': faker.name(),
        'interview': 'Not Started',
        'clientStatus': 'Brainstorming',
        'acceptance': 'In Progress',
    }
    context.page.add_invoice(context.invoice_data)


@then("I want to see saved invoice row")
def step_impl(context):
    invoice_text = context.page.get_invoice_text()
    for part in context.invoice_data.values():
        assert_in(part, invoice_text)


@then("I want to see Consultant Dashboard for chosen consultant")
def step_impl(context):
    context.execute_steps('''
        Then I want to see Consultant Dashboard page
    ''')
    assert_in(context.consultant, context.driver.page_source)

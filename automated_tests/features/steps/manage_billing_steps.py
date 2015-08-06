from behave import *
from faker import Faker
from nose.tools import assert_true, assert_equal, assert_not_in, assert_in

use_step_matcher("re")


@then("I want to see (?P<widget_name>.+) widget")
def step_impl(context, widget_name):
    widget_name = '_'.join(widget_name.split()).lower()
    assert_true(context.page.is_element_present(widget_name + '_widget'))


@when("I fill in the form with needed data")
def step_impl(context):
    fake = Faker()
    context.row_data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'fiscal_year': '2015',
        'service': '1 A La Carte Hour',
        'amount': '$950.00'
    }
    context.page.add_row(context.row_data)


@step("I closing confirmation widget")
def step_impl(context):
    context.page.close_confirmation_widget()


@then("I want to see copied record")
@then("I want to see that row at Billing Data table")
@then("I want to see edited row at Billing Data table")
@then("I want to see added row at Billing Data table")
def step_impl(context):
    ten_rows_data = [context.page.get_row_data(row_number=i) for i in range(10)]
    assert_in(context.row_data, ten_rows_data)


@then("I want to see that row has been deleted")
@then("I want to see unedited row at Billing Data table")
@then("I want to see no added row at Billing Data table")
def step_impl(context):
    context.page.wait_for_loading()
    ten_rows_data = [context.page.get_row_data(row_number=i) for i in range(10)]
    assert_not_in(context.row_data, ten_rows_data)


@step("row information on widget")
def step_impl(context):
    context.row_data['amount'] = context.row_data['amount'].replace('$', '')
    assert_equal(context.row_data, context.page.get_row_data_widget())


@then("I want to see relevant data at Billing Data table")
def step_impl(context):
    table_f_name = context.page.get_row_data()['first_name']
    assert_equal(context.search_f_name, table_f_name)


@step("fields values before editing on it")
def step_impl(context):
    for v in context.old_row_data.values():
        assert_in(v.replace('$', '').replace(',', ''), context.page.get_active_widget_text())

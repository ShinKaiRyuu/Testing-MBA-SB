from behave import *
from nose.tools import assert_in, assert_true, assert_equal, assert_not_equal

use_step_matcher("re")


@then("I want to see filtered data at (?P<table_name>.+) table")
def step_impl(context, table_name):
    context.page.wait_for_table_change()
    filtered_data = context.page.get_filtered_data(table_name=table_name, column=context.filter_type)
    assert_true(filtered_data)
    value = context.page.get_normalized_value(context.filter_value)
    if filtered_data:
        for row in filtered_data:
            assert_in(value, row)


@when("I choose (?P<date_value>.+) in (?P<start_or_end>.+) date field")
def step_impl(context, date_value, start_or_end):
    context.filter_type = getattr(context, 'filter_type', 'Date of Purchase')
    context.filter_value = getattr(context, 'filter_value', date_value)
    context.page.set_date(date_type=start_or_end, date_value=date_value)


@when("I select row")
def step_impl(context):
    context.page.select_row()
    row_data = context.page.get_row_data()
    if not hasattr(context, 'old_row_data'):
        context.old_row_data = row_data
    context.row_data = row_data


@then("I want to see widget with row information")
def step_impl(context):
    context.page.replace_bad_elements()
    widget_text = context.page.view_record_widget.text
    if isinstance(context.row_data, list):
        for field in context.row_data:
            assert_in(field, widget_text)
    elif isinstance(context.row_data, dict):
        for v in context.row_data.values():
            assert_in(v, widget_text.replace(',', ''))


@when("I fill in needed search parameters")
def step_impl(context):
    context.search_f_name = 'Joana'
    context.page.search_input.send_keys(context.search_f_name)


@step("I closing widget")
def step_impl(context):
    context.page.search_widget_close_btn.click()


@then("I want to see relevant data at Billing Report table")
def step_impl(context):
    table_f_name = context.page.get_row_data()[0]
    assert_equal(context.search_f_name, table_f_name)


@then("I want to see data with inactive consultants")
def step_impl(context):
    if hasattr(context.page, 'get_num_of_records'):
        context.num_of_records = context.page.get_num_of_records()
    else:
        context.page.save_summary_consultants_text()


@then("I want to see data without inactive consultants")
def step_impl(context):
    if hasattr(context.page, 'get_num_of_records'):
        assert_true(context.num_of_records <= context.page.get_num_of_records())
    else:
        assert_not_equal(context.page.summary_consultants_text, context.page.summary_consultants_table.text)

from behave import *
from helpers.data_helpers import modify_value

use_step_matcher("re")


@when("I trying to register with")
def step_impl(context):
    context.customer_information = {head: modify_value(row[head])
                                    for head in context.table.headings
                                    for row in context.table.rows}
    context.page.register_with(context.customer_information)


@given("I am new registered customer")
def step_impl(context):
    context.execute_steps('''
        Given I am on Registration page
        When I trying to register with
          | f_name           | l_name          | email          | password |
          | faker.first_name | faker.last_name | <unique_email> | 111111   |
        Then I want to see My Account page
    ''')

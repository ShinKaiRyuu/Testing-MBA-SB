from behave import *
from nose.tools import assert_in

use_step_matcher("re")


@step("I click Log out")
def step_impl(context):
    context.page = context.page.log_out()


@step("I want to see correct customer information")
def step_impl(context):
    customer_name = '{f_name} {l_name}'.format(**context.customer_information)
    assert_in(customer_name, context.page.customer_name.text)

from behave import *

use_step_matcher("re")


@when("I select consultant row")
def step_impl(context):
    context.consultant = context.page.select_consultant()

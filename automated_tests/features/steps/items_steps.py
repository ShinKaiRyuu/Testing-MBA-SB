from behave import *
from nose.tools import assert_true

use_step_matcher("re")


@when("I choose (?P<guide>.+) guide")
def step_impl(context, guide):
    context.page = context.page.choose_guide(guide)
    context.package = {
        'quantity': 1
    }


@step("I view (?P<guide_name>.+) details")
def step_impl(context, guide_name):
    context.page = context.page.get_item(guide_name)
    context.item_name = guide_name


@when('I choose (?P<item_name>.+) item')
def step_impl(context, item_name):
    context.item_name = item_name
    context.page = context.page.get_item(item_name)
    context.package = {
        'quantity': 1
    }


@step("I add (?P<package_name>.+) to cart")
def step_impl(context, package_name):
    context.page.remove_tag('strong')
    context.package['price'] = context.page.get_package_price(package_name)
    context.package['name'] = package_name
    context.package['data-id'] = context.page.add_package(package_name)


@step("I choose duration with (?P<duration>.+)")
def step_impl(context, duration):
    context.package['name'] = duration
    context.page.choose_duration(duration)


@step("I adding this service to cart")
def step_impl(context):
    context.package['price'] = context.page.get_service_price()
    context.page.add_service()


@step("I adding this guide to cart")
def step_impl(context):
    context.package['price'] = context.page.get_guide_price()
    context.page.add_guide()


@step("I choose class date with (?P<class_date>.+)")
def step_impl(context, class_date):
    context.package['name'] = context.page.choose_class_date(class_date)
    context.class_date = class_date


@step("I choose type of interview with (?P<interview>.+)")
def step_impl(context, interview):
    context.package['name'] = interview
    context.page.choose_interview(interview)


@step("I want to see that service is Sold out")
def step_impl(context):
    assert_true(context.page.item_is_sold_out())


@step("I choose select with (?P<option>.+)")
def step_impl(context, option):
    context.package['name'] = option
    context.page.choose_option(option)

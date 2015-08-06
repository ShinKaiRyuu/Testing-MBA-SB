from behave import *
from nose.tools import assert_in, assert_true, assert_equal, assert_not_in

use_step_matcher("re")


@then("I want to see that the guide (?P<added>.+) to the cart")
@then("I want to see that the service (?P<added>.+) to the cart")
def step_impl(context, added):
    added = False if 'not' in added else True
    cart_is_empty = context.page.cart_is_empty()
    description = ' - '.join([context.item_name, context.package.get('name', '')])

    if description.endswith(' - '):
        description = description[:-3]

    if not cart_is_empty:
        context.cart_item_text = context.page.get_cart_item(context.package.get('data-id', None))
        if added:
            assert_in(description, context.cart_item_text)
        else:
            assert_not_in(description, context.cart_item_text)


@step("consultants selects are on page")
def step_impl(context):
    assert_true(context.page.consultants_selects_on_page())


@step("prices are the same")
def step_impl(context):
    assert_equal(context.cart_item_text.count(context.package.get('price')), 2)


@step("the dates and times are the same")
def step_impl(context):
    assert_in(context.class_date, context.cart_item_text)


@when("I removing product (?P<item_name>.+)")
def step_impl(context, item_name):
    context.page.remove_product(item_name)


@step("I want to see that my cart is empty")
@then("I want to see that removed product not in cart")
def step_impl(context):
    assert_true(context.page.cart_is_empty())


@step("I choose Consultant with '(?P<c_name>.+)' and Free Consultant with '(?P<fc_name>.+)'")
def step_impl(context, c_name, fc_name):
    context.c_name = c_name
    context.fc_name = fc_name
    context.page.set_consultant(c_name)
    context.page.set_consultant(fc_name, free=True)


@when("I click Update button")
def step_impl(context):
    context.page.update_btn.click()


@step("I click Check Out button")
def step_impl(context):
    context.page.checkout_btn.click()


@then("I want to see that Consultant and Free Consultant are not changed")
def step_impl(context):
    assert_equal(context.c_name, context.page.get_consultant())
    assert_equal(context.fc_name, context.page.get_consultant(free=True))


@step("there is no Update, Checkout buttons")
def step_impl(context):
    assert_true(context.page.no_update_checkout_btns())

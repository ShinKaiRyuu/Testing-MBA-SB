from behave import *

use_step_matcher("re")


@when("I login with username '(?P<username>.+)' and password '(?P<password>.+)'")
def step_impl(context, username, password):
    kwargs = {
        'username': username,
        'password': password,
        'success': 'Unsuccessful' not in context.scenario.name
    }
    context.page.login_with(kwargs)


@given("I am logged in with username '(?P<username>.+)' and password '(?P<password>.+)'")
def step_impl(context, username, password):
    context.execute_steps('''
        Given I am on Login page
        When I login with username '{username}' and password '{password}'
        Then I want to see My Account page
    '''.format(username=username, password=password))


@then("I want be able to login with credentials above")
def step_impl(context):
    context.execute_steps('''
        When I login with username '{email}' and password '{password}'
        Then I want to see My Account page
    '''.format(**context.customer_information))


@when("I click Login button on page")
def step_impl(context):
    # print([c['name'] for c in context.driver.get_cookies()])
    context.page.to_login_form_btn.click()


@given("I am logged in as administrator")
def step_impl(context):
    context.execute_steps('''
        Given I am on Scoreboard Main page
        When I click Login button on page
        And I login with username 'Agrossman' and password '111111'
        Then I want to see Billing Reporting page
    ''')


@given("I am logged in as consultant")
def step_impl(context):
    context.execute_steps('''
        Given I am on Scoreboard Main page
        When I click Login button on page
        And I login with username 'Jkedrowski' and password '111111'
        Then I want to see Consultant Dashboard page
    ''')

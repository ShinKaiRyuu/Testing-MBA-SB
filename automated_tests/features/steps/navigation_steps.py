from behave import *
from nose.tools import assert_in
from selenium.common.exceptions import TimeoutException
from webium.driver import close_driver, get_driver

from helpers.driver_helpers import get_updated_driver
from pages.shopify import (
    FreeConsultationPage, MyAccountPage, LoginPage, MainPage, RegistrationPage, ServicesPage,
    CartPage, GuidesPage, CompletePurchasePage, CheckoutPage)
from pages.scoreboard import (
    ScoreboardMainPage, BillingReportingPage, ConsultantDashboardPage, ConsultantSummaryReportPage,
    ConsultantAdminDashboardPage, ManageBillingPage, ClientReportingPage)

use_step_matcher("re")

PAGES_MAP = {
    'Free Consultation': FreeConsultationPage,
    'Login': LoginPage,
    'My Account': MyAccountPage,
    'Main': MainPage,
    'Registration': RegistrationPage,
    'Services': ServicesPage,
    'Guides': GuidesPage,
    'Cart': CartPage,
    'Check Out': CheckoutPage,
    'Complete My Purchase': CompletePurchasePage,
    'Scoreboard Main': ScoreboardMainPage,
    'Billing Reporting': BillingReportingPage,
    'Consultant Dashboard': ConsultantDashboardPage,
    'Consultant Summary Report': ConsultantSummaryReportPage,
    'Consultant Administrator Dashboard': ConsultantAdminDashboardPage,
    'Manage Billing': ManageBillingPage,
    'Client Reporting': ClientReportingPage
}


@when("I open (?P<page_name>.+) page")
@step("I am on (?P<page_name>.+) page")
def step_impl(context, page_name):
    context.page_name = page_name
    page = PAGES_MAP[page_name]
    context.page = page()

    success = None
    while not success:
        try:
            context.page.open()
            success = True
        except TimeoutException:
            print('caught TimeoutException')
            close_driver()
            context.driver = get_updated_driver()

    iframe = getattr(context.page, 'iframe', None)
    if iframe:
        context.driver.switch_to.frame(iframe)

    default_wait_for_page = getattr(context.page, 'default_wait', None)
    if default_wait_for_page:
        default_wait_for_page()


@then("I want to see (?P<page_name>.+) page")
def step_impl(context, page_name):
    page = PAGES_MAP[page_name]
    context.page = page()
    assert_in(page.url, get_driver().current_url)


@step("I view my cart")
def step_impl(context):
    context.execute_steps('''
        Given I am on Cart page
    ''')

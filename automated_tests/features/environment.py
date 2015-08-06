from datetime import datetime
from sys import platform
from webium.driver import get_driver
from helpers.email_tools.mandrill_email import get_emails_number
from helpers.driver_helpers import get_updated_driver


def before_all(context):
    if 'linux' in platform:
        from pyvirtualdisplay import Display

        context.xvfb = Display(visible=0, size=(1366, 768)).start()
    else:
        context.save_screenshots = False
        context.close_after_all = False

    context.driver = get_updated_driver()


def before_scenario(context, scenario):
    if 'new emails' in str(scenario.steps):
        context.emails_number = get_emails_number()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        if getattr(context, 'save_screenshots', True):
            take_screenshot(scenario, context.step_name)
    delete_cookies()


def before_step(context, step):
    context.step_name = step.name


def after_all(context):
    if getattr(context, 'close_after_all', True):
        get_driver().quit()

    if hasattr(context, 'xvfb'):
        context.xvfb.stop()


def take_screenshot(scenario, step_name):
    scenario_name = scenario.name.replace('@', '')
    feature_filename = scenario.filename.split('/')[-1].split('.')[0]
    datetime_part = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    dir_name = './test-results/screenshots'
    get_driver().get_screenshot_as_file('{0}/{1}__{2}__{3}__{4}.png'.format(
        dir_name, datetime_part, feature_filename, scenario_name, step_name))


def delete_cookies():
    driver = get_driver()
    cookies_to_delete = [c['name'] for c in driver.get_cookies() if c['name'] != 'storefront_digest']
    for c in cookies_to_delete:
        driver.delete_cookie(c)

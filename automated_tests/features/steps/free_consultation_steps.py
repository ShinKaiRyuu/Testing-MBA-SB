from collections import OrderedDict
from behave import *
from helpers.data_helpers import make_ordered_dict, modify_value
from helpers.files import get_full_path

use_step_matcher("re")


@when(
    "I fill part of Contact information with (?P<f_name>.+), (?P<l_name>.+), (?P<email>.+), "
    "(?P<phone>.+), (?P<password>.+), (?P<repeat_pass>.+)")
def step_impl(context, f_name, l_name, email, phone, password, repeat_pass):
    context.fc_data = OrderedDict()
    keys = ['f_name', 'l_name', 'email', 'phone', 'password', 'repeat_pass']
    kwargs = make_ordered_dict(keys, locals())
    context.email = kwargs.get('email')
    free_c_page = context.page
    free_c_page.fill_contact_information(first=True, **kwargs)
    context.fc_data.update(kwargs)


@step(
    "I fill another part of Contact information with (?P<hear_how>.+), (?P<cons_name>.+), (?P<subscr>.+), "
    "(?P<programs>.+), (?P<month>.+), (?P<year>.+)")
def step_impl(context, hear_how, cons_name, subscr, programs, month, year):
    keys = ['hear_how', 'cons_name', 'subscr', 'programs', 'month', 'year']
    kwargs = make_ordered_dict(keys, locals())
    context.page.fill_contact_information(**kwargs)
    context.fc_data.update(kwargs)


@step("I fill Academic Information with (?P<instit>.+), (?P<gpa>.+), (?P<major>.+), (?P<YoG>.+)")
def step_impl(context, instit, gpa, major, YoG):
    keys = ['instit', 'gpa', 'major', 'YoG']
    kwargs = make_ordered_dict(keys, locals())
    context.page.fill_academic_information(**kwargs)
    context.fc_data.update(kwargs)


@step("I choose (?P<gmat_gre>.+) of GMAT/GRE")
def step_impl(context, gmat_gre):
    context.page.select_option_or_radio('gmat_gre', {'gmat_gre': gmat_gre})
    context.fc_data['gmat_gre'] = gmat_gre


@step("I fill Post-MBA Career Goals with (?P<goals>.+)")
def step_impl(context, goals):
    context.page.clear_send_keys('goals', {'goals': modify_value(goals)})
    context.fc_data['goals'] = goals


@step("I fill Resume Upload with (?P<resume>.+), (?P<comments>.+)")
def step_impl(context, resume, comments):
    context.page.resume.send_keys(get_full_path(resume))
    context.page.clear_send_keys('comments', {'comments': modify_value(comments)})
    context.fc_data['comments'] = comments


@step("I fill captcha with (?P<c>.+)")
def step_impl(context, c):
    context.page.captcha.send_keys(c)

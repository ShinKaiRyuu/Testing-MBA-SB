from behave import *
from nose.tools import assert_equal, assert_in
import time
from helpers.email_tools.mandrill_email import get_emails_number, get_email_html, get_emails
from helpers.email_tools import free_consultation_email as fc_email

use_step_matcher("re")


@step("as administrator I want to receive (?P<emails_number>.+) new emails")
def step_impl(context, emails_number):
    emails_number = int(emails_number)
    context.new_email = get_emails_number() - context.emails_number

    if emails_number:
        for attempt in range(100):
            e = get_emails(limit=1)
            sender = e[0].get('sender')
            if context.emails_number == get_emails_number() or sender != context.email:
                time.sleep(15)
                print('-' * 50)
                print('before - {}'.format(context.emails_number), 'after - {}'.format(get_emails_number()))
                print(e)
            else:
                print('{} attempts'.format(attempt))
                context.new_email = get_emails_number() - context.emails_number
                break
        print('From: {}'.format(context.email))

    assert_equal(emails_number, context.new_email)


@step("I want to see Free Consultation data in email if email received")
def step_impl(context):
    if context.new_email:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(get_email_html())
        email_text = '\n'.join(line.strip() for line in soup.get_text().split('\n'))

        for k, v in context.fc_data.items():
            if v == 'empty':
                context.fc_data[k] = '\n'
        context.fc_data['programs_list'] = ' '.join([pr for pr in context.fc_data.get('programs')])
        if context.fc_data['gmat_gre'] in ['gmat', 'gre']:
            context.fc_data['gmat_gre'] = context.fc_data['gmat_gre'].upper()

        for field in ['comments', 'goals']:
            if context.fc_data[field] != '\n':
                context.fc_data[field] = ''.join(['\n', context.fc_data[field]])

        assert_in(fc_email.customer_request.format(**context.fc_data), email_text)
        assert_in(fc_email.contact_information.format(**context.fc_data), email_text)
        assert_in(fc_email.plans.format(**context.fc_data), email_text)
        assert_in(fc_email.academic_information.format(**context.fc_data), email_text)
        assert_in(fc_email.other.format(**context.fc_data)[1:-1], email_text)

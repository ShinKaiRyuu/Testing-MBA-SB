from datetime import datetime
import mandrill
import time


API_KEY = '6SQnRPmeZI5IEffpnEWv4Q'
TO_EMAIL = 'anton.podobytko@gmail.com'
_mandrill_client = None


def get_email_html(**kwargs):
    messages = get_emails(limit=1, **kwargs)
    _id = messages[0]['_id']

    email_html = None
    while email_html is None:
        try:
            email_html = get_client().messages.content(id=_id).get('html')
            return email_html
        except mandrill.UnknownMessageError:
            print('caught mandrill.UnknownMessageError')
            time.sleep(5)


def get_emails_number(**kwargs):
    return len(get_emails(**kwargs))


def get_emails(**kwargs):
    today = datetime.now().strftime('%Y-%m-%d')
    email = kwargs.get('email') or TO_EMAIL
    kwargs.pop('email', None)
    return get_client().messages.search(query='email:{}'.format(email), date_from=today, **kwargs)


def get_client():
    global _mandrill_client
    if not _mandrill_client:
        _mandrill_client = mandrill.Mandrill(API_KEY)
    return _mandrill_client


if __name__ == '__main__':
    # t = get_email_text(email='fdenx7@bladesmail.net')
    # t = get_email_html()
    print(get_emails(limit=3))
    print(get_emails_number())

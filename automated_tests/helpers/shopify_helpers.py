import datetime
import requests
from bs4 import BeautifulSoup

URL = 'https://block-six-analytics.myshopify.com/admin/{}'
PAYLOAD = {
    'login': 'adam.grossman@blocksixanaltyics.com',
    'password': 'sherman11',
    'redirect': '',
    'utf8': '%E2%9C%93',
    'authenticity_token': None
}
LOGIN_URL = URL.format('auth/login')
ORDERS_URL = URL.format('orders')


def _shopify_session():
    s = requests.Session()
    r = s.get(LOGIN_URL)
    soup = BeautifulSoup(r.content)
    token = soup.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
    PAYLOAD['authenticity_token'] = token
    s.post(LOGIN_URL, data=PAYLOAD)
    return s


def get_shopify_orders(orders_number=-1):
    s = _shopify_session()
    r = s.get(ORDERS_URL)
    soup = BeautifulSoup(r.content)
    tr_tags = soup.select('tr[class]')

    if orders_number > 0:
        tr_tags = tr_tags[:orders_number]

    orders = [
        {
            'order': _get_order_details(session=s, url=tr.select('td.order a')[0].get('href')),
            'date': _get_order_date(tr.select('td.date span')[0].get('title')),
            'customer': {
                'name': tr.select('.customer-name a.subdued')[0].get_text().strip(),
                'url': tr.select('.customer-name a.subdued')[0].get('href'),
                'email': tr.select('a.subdued.dropdown-unstyled-link')[0].get_text().strip(),
            },
            'payment_status': tr.select('span.badge')[0].get_text().replace('\n', '').strip(),
            'total': tr.select('.total')[0].get_text().strip()
        }
        for tr in tr_tags
        ]

    return orders


def _get_order_date(order_date):
    order_date = ' '.join(order_date.split()[:-1])
    order_date = datetime.datetime.strptime(order_date, '%B %d, %Y').strftime('%m-%d-%Y')
    return {
        'order_date': order_date,
        'fiscal_year': _get_fiscal_year(order_date)
    }


def _get_fiscal_year(order_date):
    m, d, y = map(int, order_date.split('-'))
    if m <= 5 and d <= 31:
        return str(y - 1)
    else:
        return str(y)


def _get_order_details(session, url):
    order_transaction = url.split('/')[-1]
    order_url = '/'.join(['orders', order_transaction])
    r = session.get(URL.format(order_url))
    soup = BeautifulSoup(r.content)

    try:
        return {
            'transaction': order_transaction,
            'product': soup.select('p.subdued')[0].get_text().strip(),
            'consultant': soup.select('div[context=note_0] textarea.next-textarea')[0].get_text().strip(),
            'free_consultant': soup.select('div[context=note_1] textarea.next-textarea')[0].get_text().strip(),
            'parsed': True
        }
    except IndexError:
        return {'parsed': False}


if __name__ == '__main__':
    from pprint import pprint

    some_orders = get_shopify_orders(orders_number=3)
    pprint(some_orders)

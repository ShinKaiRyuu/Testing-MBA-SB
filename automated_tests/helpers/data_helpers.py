from ast import literal_eval
from collections import OrderedDict
from tempmail import TempMail
from faker import Faker

_faker = None


def make_ordered_dict(keys, _locals):
    kwargs = OrderedDict()
    for key in keys:
        value = _locals.get(key)
        kwargs[key] = modify_value(value)
    return kwargs


def modify_value(value):
    if '[' in value:
        return literal_eval(value.replace('empty', ' '))
    elif 'empty' in value:
        return ''
    elif 'spaces' in value:
        return ' ' * int(value.split(':')[-1][:-1])
    elif 'unique_email' in value:
        return TempMail().get_email_address()
    elif 'faker' in value:
        faker = get_faker()
        faker_attr = value.split('.')[-1]
        return getattr(faker, faker_attr)().split('\n')[0]
    else:
        return value


def get_faker():
    global _faker
    if not _faker:
        _faker = Faker()
    return _faker

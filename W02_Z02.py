import datetime
from functools import wraps

def add_date(format):
    def inner(to_be_decorated):
        @wraps(to_be_decorated)
        def wrapper(*args, **kwargs):
            val = to_be_decorated(*args, **kwargs)
            val['date'] = datetime.datetime.now().strftime(format)
            return val
        return wrapper
    return inner

@add_date('%B %Y')
def get_data(a):
    return {1: a, 'name': 'Jan'}


assert get_data(2) == {
    1: 2, 'name': 'Jan', 'date': 'April 2020'
}

print(get_data(2))
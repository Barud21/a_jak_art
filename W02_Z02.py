from functools import wraps

def is_correct(*args):
    def inner(f):
        @wraps(f)
        def wrapper():
            dictionary = f()
            if all(arg in dictionary for arg in args):
                return dictionary
            else:
                return None
        return wrapper
    return inner

@is_correct('first_name', 'last_name')
def get_data():
    return {
        'first_name': 'Jan',
        'last_name': 'Kowalski',
        'email': 'jan@kowalski.com'
    }


@is_correct('first_name', 'last_name', 'email')
def get_other_data():
    return {
        'first_name': 'Jan',
        'email': 'jan@kowalski.com'
    }


assert get_data() == {
    'first_name': 'Jan',
    'last_name': 'Kowalski',
    'email': 'jan@kowalski.com'
}


assert get_other_data() is None

print(get_other_data())
print(get_data())
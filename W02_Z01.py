def wraps(actual_decorated_function):
    def decor(decorated_function):
        decorated_function.__name__ = actual_decorated_function.__name__
        decorated_function.__module__ = actual_decorated_function.__module__
        decorated_function.__doc__ = actual_decorated_function.__doc__
        decorated_function.__qualname__ = actual_decorated_function.__qualname__
        decorated_function.__annotations__ = actual_decorated_function.__annotations__
        return decorated_function
    return decor


def bumelant(*args, **kwargs):
    def wrap(to_be_decorated):
        @wraps(to_be_decorated)
        def wrapper(*args, **kwargs):
            return to_be_decorated(*args, **kwargs)
        return wrapper
    return wrap


@bumelant(1, 2)
def say_python():
    """jakis opis"""
    return "PYTHON"


assert say_python.__doc__ == "jakis opis"
print(say_python.__doc__)
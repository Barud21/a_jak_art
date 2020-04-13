from functools import wraps

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
print(say_python.__module__)

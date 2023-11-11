# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
# являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр
# precision
# , который указывает, до скольки цифр после запятой округлять числа.

from functools import wraps


def round_integer(predicate):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (float, int)):
                return round(result, predicate)
            elif isinstance(result, (tuple, list)):
                return [round(i, predicate) for i in result if isinstance(i, (float, int))]
            else:
                raise TypeError('Error type send argument')
        return inner
    return wrapper


@round_integer(predicate=2)
def foo():
    #return 4.1234
    return [2.3243263563, 4.1, 5, 12.8545635, 'fg', '23']


print(foo())

# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
# являются целыми, и округляет их до целых, если это не так.

def check_integer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (float, int)):
            return round(result)
        elif isinstance(result, (tuple, list)):
            return [round(i) for i in result if isinstance(i, (float, int))]
        else:
            raise TypeError('Error type send argument')

    return inner


@check_integer
def test_one():
    return [2.3, 4, 5, 12.8, 'fg', '23']


print(test_one())

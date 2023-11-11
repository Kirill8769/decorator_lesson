# Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время,
# если произошла ошибка. Параметры, передаваемые в декоратор, обязательно должны быть именованными.

from functools import wraps
import time


def retry(*, retries=3, delay=3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(delay)
            raise Exception('Function call failed after multiple retries.')

        return inner

    return wrapper


COUNT = 0


@retry(retries=3, delay=1)
def foo():
    global COUNT
    if COUNT in [0, 1]:
        COUNT += 1
        raise Exception
    return 'Success'


print(foo())

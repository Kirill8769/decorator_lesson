# Создайте декоратор @memoize, который кэширует результаты функции для определенных аргументов.
# Если функция вызывается с теми же аргументами, что и в прошлый раз,
# она должна возвращать результат из кэша, а не вычислять его заново.
# Также создайте два дополнительных декоратора:
#     @slowit(n) - декоратор с параметрами, которые замедляет работу функции на n секунд.
#     Без параметров декоратор замедляет функцию на 1 секунду. В декораторе используется time.sleep(n).
#
#     @timeit - декоратор, который выводит время работы функции.

from functools import reduce, wraps
import time


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return wrapper


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} executed in {end_time - start_time: .6f} seconds")
        return result

    return wrapper


def slowit(slow=1):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            time.sleep(slow)
            return func(*args, **kwargs)

        return inner

    return wrapper


# Без кэширования время работы функции при каждом вызове не менее 2 секунд.
@timeit
@memoize
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else None


print(product(5))
print(product(5))

# С кэшированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
@timeit
@memoize
@slowit(4)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)

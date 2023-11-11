# Создайте декоратор @logging, который будет логировать вызовы функции и её результат.
# Лог должен выводиться на экран.


def logging(func):
    def wrapper(*args: tuple, **kwargs: dict):
        print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. Result: {func(*args, **kwargs)}")
    return wrapper


@logging
def multiply(x, y):
    return x * y


multiply(2, 3) # печатает "Function multiply called with args: (2, 3) and kwargs: {}. Result: 6"

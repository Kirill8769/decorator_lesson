# Создайте декоратор @positive_integers, который проверяет,
# что все аргументы функции - положительные целые числа.


def positive_integers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError("All arguments must be positive integers")
        return func(*args)
    return wrapper


@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(2, 3, 4)) # 24
print(multiply(2, 0, 4)) # Выбрасывает исключение ValueError с сообщением "All arguments must be positive integers"

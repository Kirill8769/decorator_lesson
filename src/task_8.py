# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до определенной длины.
# Если слово было сокращено, в конце слова ставится переданный символ.
# Количество символов в слове и знак в конце сокращенного слова — параметры декоратора.
# Причем символ обязательно должен передаваться как именованный аргумент.

from functools import wraps

def shorten_word(max_len, *, end_symbol='.'):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result: str = func(*args, **kwargs)
            return " ".join([word[:max_len] + end_symbol if len(word) > max_len else word for word in result.split()])
        return inner
    return wrapper


@shorten_word(4, end_symbol=' (.)(.) ')
def foo():
    return 'Sasha was walking on highway, and sucked bagel'


print(foo())

# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до 4 символов. Если слово было сокращено, в конце слова ставится точка.

def shorten_word(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return " ".join([word[:4] for word in result.split()])

    return wrapper


@shorten_word
def foo():
    return 'Sasha was walking on highway, and sucked bagel'


print(foo())

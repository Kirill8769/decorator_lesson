# Напишите три декоратора, которые можно применять последовательно к результату декорируемой функции.
# Первый декоратор должен заменять в тексте, который выдает функция, все восклицательные знаки ! на !!!.
# Второй декоратор должен заменять в тексте, который выдает функция, все знаки вопроса ? на ???.
# Третий декоратор должен заменять в тексте, который выдает функция, все точки . на ... .

def change_the_exclamation_mark(func):
    def wrapper(*args, **kwargs):
        result: str = func(*args, **kwargs)
        return result.replace("!", "!!!")
    return wrapper




def change_the_question_mark(func):
    def wrapper(*args, **kwargs):
        result: str = func(*args, **kwargs)
        return result.replace("?", "???")
    return wrapper


def change_the_dots(func):
    def wrapper(*args, **kwargs):
        result: str = func(*args, **kwargs)
        return result.replace(".", "...")
    return wrapper


text = "Первый декоратор-!\nВторой декоратор-?\nТретий декоратор-."


@change_the_dots
@change_the_question_mark
@change_the_exclamation_mark
def foo():
    return text


print(foo())

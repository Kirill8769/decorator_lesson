# Напишите декоратор, который позволяет возвращать элементы декорируемой
# функции по одному через yield,
# если эта функция возвращает список или кортеж.

def yield_item(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            for res in result:
                yield res
        else:
            yield result
    return wrapper


@yield_item
def foo():
    return [i for i in range(5)]


gen = foo()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Напишите декоратор, который повторно вызывает декорируемую функцию три раза, 
# каждый раз через три секунды, если произошла ошибка.

import time


def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)                
            except Exception as ex:
                time.sleep(3)    
        raise Exception('Tried it three times, failed')    
    return wrapper


COUNT = 0
@retry
def foo():
    global COUNT
    if COUNT in [0, 1]:
        COUNT += 1
        raise Exception
    return 'Success'


print(foo())

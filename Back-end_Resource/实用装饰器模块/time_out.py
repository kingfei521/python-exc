import functools
from concurrent import futures

executor = futures.ThreadPoolExecutor(1)

def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)
        return wrapper
    return decorator

import time

@timeout(1)
def task(a, b):
    try:
        time.sleep(1.1)
        return a + b
    except TimeoutError as e:
        print(e)



print(task(2, 3))


# 2================
"""
注意：使用 @functools.wraps 的目的是因为被装饰的 func 函数元信息会被替换为 wrapper 函数的元信息，而 @functools.wraps(func) 
将 wrapper 函数的元信息替换为 func 函数的元信息。最终虽然返回的是 wrapper 函数，元信息却依然是原有的 func 函数
在函数式编程中，函数的返回值是函数对象被称为闭包
"""
import functools
from concurrent import futures

class timeout:
    __executor = futures.ThreadPoolExecutor(1)

    def __init__(self, seconds):
        self.seconds = seconds

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = timeout.__executor.submit(func, *args, **kw)
            return future.result(timeout=self.seconds)
        return wrapper
import time
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"函数 {func.__name__} 耗时 {(end - start) * 1000} ms")
        return res
    return wrapper

@log
def now():
    for i in range(10000):
        pass
    print('运行结束……')

now()
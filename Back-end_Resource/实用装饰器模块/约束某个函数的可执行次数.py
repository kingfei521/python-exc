"""
如果我们希望程序中的某个函数在整个程序的生命周期中只执行一次或 N 次，可以写一个这样的装饰器
"""

import functools

class Allow_count:
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if self.i >= self.count:
                return
            self.i += 1
            return func(*args, **kw)
        return wrapper

# 测试

@Allow_count(3)
def job(x):
    x += 1
    return x

for i in range(10):
    print(job(i))
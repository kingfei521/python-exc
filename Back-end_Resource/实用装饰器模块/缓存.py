import math
import random
import time
from functools import lru_cache


@lru_cache()  # 缓存装饰器自带的
def task(x):
    time.sleep(0.01)
    return round(math.log(x**3 / 15), 4)


for i in range(500):
    task(random.randrange(5, 10))


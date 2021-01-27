import json
import threading

from template import *
from faker import Faker
fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN', 'en_CA', 'en_PH', 'en_TH', 'uk_UA'])

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance


class File(metaclass=SingletonType):
    def __init__(self, file_name):
        self.name = file_name

    def save_data_json(self, row, field):

        data = {}
        with open(self.name + '.json', 'w') as f:
            for i in range(0, int(row)):
                for k, v in field.items():
                    data[k] = data_generator(v)
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')


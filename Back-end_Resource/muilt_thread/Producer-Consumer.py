import concurrent.futures
import logging
import random
import threading

SENTINEL = object()

""""
自定义实现管道
"""
class Pipeline(object):
    """
    允许在生产者和消费者之间使用单个元素管道的类。
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s: about to acquire getlock", name)
        self.consumer_lock.acquire()

        logging.debug('%s:have getlock', name)
        message = self.message

        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()

        logging.debug('%s:setlock release', name)
        return message

    def set_message(self, message, name):
        logging.debug('%s:about to acquire setlock', name)
        self.producer_lock.acquire()

        logging.debug('%s:have setlock', name)
        self.message = message

        logging.debug('%s:about to release getlock', name)
        self.consumer_lock.release()

        logging.debug("%s:getlock released", name)


def producer(pipeline):
    """Pretend we`re getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # 发送前哨消息以告知消费者我们已经完成
    pipeline.set_message(SENTINEL, "Producer")
def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
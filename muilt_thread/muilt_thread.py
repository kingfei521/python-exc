import logging
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    """
    * 使用for循环创建多个线程
    *
    """

    # threads = list()
    # for index in range(3):
    #     logging.info('Main   : create and start thread %d.', index)
    #     x = threading.Thread(target=thread_function, args=(index, ))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main   : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main   : thread %d done", index)

    """
    * 有一种更简单的方法来启动一组线程。它称为ThreadPoolExecutor，
    * 并且是concurrent.futures（自Python 3.2起）标准库的一部分。
    *
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
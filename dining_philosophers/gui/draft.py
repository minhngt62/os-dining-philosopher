# SuperFastPython.com
# example of logging from multiple processes in a process-safe manner
from random import random
from time import sleep
from multiprocessing import current_process
from multiprocessing import Process
from multiprocessing import Queue
from logging.handlers import QueueHandler
import logging
 
# executed in a process that performs logging
def logger_process(queue):
    # create a logger
    logger = logging.getLogger('app')
    # configure a stream handler
    logger.addHandler(logging.StreamHandler())
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)
    # run forever
    while True:
        # consume a log message, block until one arrives
        message = queue.get()
        # check for shutdown
        if message is None:
            break
        # log the message
        logger.handle(message)
 
# task to be executed in child processes
def task(queue):
    # create a logger
    logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)
    # get the current process
    process = current_process()
    # report initial message
    logger.info(f'Child {process.name} starting.')
    # simulate doing work
    for i in range(5):
        # report a message
        logger.debug(f'Child {process.name} step {i}.')
        # block
        sleep(random())
    # report final message
    logger.info(f'Child {process.name} done.')
 
# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # create a logger
    logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)
    # start the logger process
    logger_p = Process(target=logger_process, args=(queue,))
    logger_p.start()
    # report initial message
    logger.info('Main process started.')
    # configure child processes
    processes = [Process(target=task, args=(queue,)) for i in range(5)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
    # report final message
    logger.info('Main process done.')
    # shutdown the queue correctly
    queue.put(None)
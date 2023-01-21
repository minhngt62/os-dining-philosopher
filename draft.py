from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Manager
 
# task executed in a new process
def task(number, shared_lock):
    # acquire the shared lock
    with shared_lock:
        # generate a number between 0 and 1
        value = random()
        # block for a fraction of a second
        sleep(value)
        # report the generated value
        print(f'{number} got {value}')
 
# protect the entry point
if __name__ == '__main__':
    # create the manager
    with Manager() as manager:
        # create the shared mutex lock
        shared_lock = manager.Lock()
        # create many child processes
        processes = [Process(target=task, args=(i, shared_lock)) for i in range(10)]
        # start all processes
        for process in processes:
            process.start()
        # wait for all processes to complete
        for process in processes:
            process.join()
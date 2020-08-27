import threading
import time
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            #要执行的话就需要去队列里面取了
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def moyu():
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def queue_pool():
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True) #每个线程都让它们处于守护状态
        t.start()

    for i in range(20):
        queue.put(moyu)
    queue.join()

if __name__ == '__main__':
    queue_pool()
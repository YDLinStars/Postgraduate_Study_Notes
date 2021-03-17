import  threading
import  time

#创建一个线程子类：
from concurrent.futures.thread import ThreadPoolExecutor


class MyThread(threading.Thread):
    def __init__(self,threadID,name,couter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.couter = couter

    def run(self):
        print("开始线程： "+self.name)
        moyu_time(self.name, self.couter, 10)
        print("退出线程："+self.name)

def moyu_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s 开始摸鱼 %s" % (threadName,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            counter -= 1


if __name__ == '__main__':
    pool = ThreadPoolExecutor (29)
    for i  in range(1,5):
        pool.submit(moyu_time(('YDLin'+str(i)),1,3))

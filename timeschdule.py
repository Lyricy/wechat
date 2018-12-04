from datetime import datetime
import random
import itchat
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
def tick():
    room = itchat.search_chatrooms(name='天才与白痴')[0]
    itchat.send('消息轰炸', room['UserName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.update_chatroom(True)
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick, 'interval', seconds=2)
    # 这里的调度任务是独立的一个线程
    scheduler.start()
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            print('send...')
    except:
        scheduler.shutdown()
        print('Exit The Job!')

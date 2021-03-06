#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import sys, imp,redis
reload(sys)
sys.setdefaultencoding('utf8')

class MyWXBot(WXBot):
    def __init__(self):
        WXBot.__init__(self)
        self.redis = redis.Redis(host='localhost',port=6379,db=0)
    # def __init__(self):
        # WXBot.__init__(self)
        # self.auto_send_message()

    # def schedule(self):
    #     res = self.db.execute("SELECT * FROM zml_qun_user WHERE Uin=%s",['27287265'])
    #     row = res.fetchone()
    #     if row:
    #         UserName = row['UserName']
    #         while True:
    #             time.sleep(100)
    #             try:
    #                 self.send_msg_by_uid(u'维护消息'+str(time.time()),row['UserName'],1)
    #             except Exception:
    #                 print 'auto message error'
    #                 pass

    def handle_msg_all(self, msg):
        try:
            bot = imp.load_module('bot',*imp.find_module('bot'))
            mybot = bot.bot(self)
            mybot.handle_msg_all(self, msg)
        except Exception as e:
            print 'error=',e

    def schedule(self):
        try:
            bot = imp.load_module('bot',*imp.find_module('bot'))
            mybot = bot.bot(self)
            mybot.schedule(self)
        except Exception as e:
            print 'error=',e

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    # print 'start'
    # s = redis.Redis(host='localhost',port=6379,db=0)
    # s.set('a11', 123)
    # print s.get('a11')
    main()

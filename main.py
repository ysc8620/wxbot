#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import sys, imp
reload(sys)
sys.setdefaultencoding('utf8')

class MyWXBot(WXBot):
    # def __init__(self):
        # WXBot.__init__(self)
        # self.auto_send_message()

    def schedule(self):
        res = self.db.execute("SELECT * FROM zml_qun_user WHERE Uin=%s",['27287265'])
        row = res.fetchone()
        if row:
            UserName = row['UserName']
            while True:
                time.sleep(100)
                try:
                    self.send_msg_by_uid(u'维护消息'+str(time.time()),row['UserName'],1)
                except Exception:
                    print 'auto message error'
                    pass



    def handle_msg_all(self, msg):
        try:
            bot = imp.load_module('bot',*imp.find_module('bot'))
            mybot = bot.bot()
            mybot.handle_msg_all(self, msg)
        except Exception as e:
            print 'error=',e

    def schedule(self):
        print '-----------------'
        # if(time.time())
        res = self.db.execute("SELECT * FROM zml_qun_user WHERE Uin=%s",['234004768'])
        row = res.fetchone()
        if row:
            try:
                print row['NickName'], row['UserName']
                self.send_msg_by_uid(u'维护消息'+str(time.time()),row['UserName'],1)
            except Exception:
                print 'auto message error'
                pass
        time.sleep(60)



def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    print 'start'
    main()

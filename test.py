#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        print '----'
        print msg
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid('hi', msg['user']['id'])

    def schedule(self):
        self.send_msg(u'机器猫', 'schedule')
        time.sleep(60)



def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()

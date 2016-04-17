#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import sys, imp
reload(sys)
sys.setdefaultencoding('utf8')

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        try:
            bot = imp.load_module('bot',*imp.find_module('bot'))
            mybot = bot.bot()
            self.get_contact_info()
            mybot.handle_msg_all(self, msg)
        except Exception:
            pass

    def schedule(self):
        try:
            bot = imp.load_module('bot',*imp.find_module('bot'))
            mybot = bot.bot()
            mybot.schedule(self)
        except Exception:
            pass



def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    print 'start'
    main()

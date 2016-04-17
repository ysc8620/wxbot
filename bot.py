#!/usr/bin/env python
# coding: utf-8

import sys, time, requests, json, ConfigParser,re
from db import *
reload(sys)
sys.setdefaultencoding('utf8')

class bot():
    def __init__(self):
        try:
            self.session = requests.Session()
            self.session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5'})
            self.command_list = []
            self.db = DB()
            cf = ConfigParser.ConfigParser()
            cf.read('base.ini')
            self.api_url = cf.get('base','url')
            self.command_path = cf.get('base','command_path')
            fopen = open(self.command_path)
            try:
                command_str = fopen.read()
                self.command_list = json.loads(command_str)
            finally:
                 fopen.close( )
        except Exception:
            pass

    def handle_msg_all(self, wxbot, msg):
        print msg
        # ge ren xiao
        # if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
        #     self.send_msg_by_uid('hi', msg['user']['id'])

        # 群消息处理
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            data = {
                'msg' : msg
            }
            try:
                # 匹配是否是命令行
                for command in self.command_list:
                    pattern = re.compile(r"\s*"+command+"\s*")
                    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
                    match = pattern.match(msg['content']['data'])
                    if match:
                        re = self.session.post(self.api_url, data)
                        re.encoding = 'utf-8'
                        result = json.loads(re.text.encode('utf-8'))
                        if result['msg_code'] == 10001:
                            wxbot.send_msg_by_uid(result['data']['message'], result['data']['uid'],result['data']['type'],result['data']['expand'])

            except Exception:
                # ji
                pass


    def schedule(self, wxbot):
        #wxbot.send_msg('群助理','')
        time.sleep(10)

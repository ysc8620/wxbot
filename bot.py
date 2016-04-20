#!/usr/bin/env python
# coding: utf-8

import sys, time, requests, json, ConfigParser,re,hashlib
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

            self.api = cf.get('base','api')
            self.appsecret = cf.get('base','appsecret')

            self.command_path = cf.get('base','command_path')
            fopen = open(self.command_path)
            try:
                command_str = fopen.read()
                self.command_list = json.loads(command_str)
            finally:
                 fopen.close( )
        except Exception as e:
            print 'error=',e

    def handle_msg_all(self, wxbot, msg):
        # ge ren xiao
        # if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
        #     self.send_msg_by_uid('hi', msg['user']['id'])

        # 群消息处理
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            data = {
                'msg' : json.dumps(msg),
                'api' : self.api,
                'time' : int(time.time())
            }
            #print data
            try:
                # 匹配是否是命令行
                for c in self.command_list:
                    pattern = re.compile(r"^\s*"+u""+c['command']+"\s*$")
                    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
                    match = pattern.match(msg['content']['data'])
                    if match:
                        print c['remark']
                        res = self.session.post(self.api_url, data)
                        res.encoding = 'utf-8'
                        print res.text
                        result = json.loads(res.text.encode('utf-8'))
                        #print result
                        if result['msg_code'] == 10001:
                            wxbot.send_msg_by_uid(result['data']['message'], result['data']['uid'],result['data']['type'],result['data']['expand'])

            except Exception as e:
                print 'error=',e


    def schedule(self, wxbot):
        #wxbot.send_msg('群助理','')
        time.sleep(10)

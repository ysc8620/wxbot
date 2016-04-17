#!/usr/bin/python
#coding=utf-8
import sys,os
import time
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb

def logs(str):
    print str
    file("./error.log","a+").write(str+"\r")

class DB:
    conn = None
    cursor = None
    Object = None

    def __init__(self):
        self.connect()

    #self.conn = MySQLdb.connect(user='24a',db='test',passwd='24abcdef',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
    def connect(self):
        self.conn = MySQLdb.connect(user = 'root',db='zhimale',passwd = 'LEsc2008',host='localhost')
        #self.conn = MySQLdb.connect(user='root',db='test',passwd='ntucdbs911',host='localhost',unix_socket='/tmp/mysql.sock')

    def execute(self, sql, args=None):
        """
        :rtype : object
        """
        try:
            self.cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            self.cursor.execute('SET NAMES utf8')
        except Exception, e:
            print '---------------'+e.message
            self.connect()
            self.cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            self.cursor.execute('SET NAMES utf8')

        try:
            if args is not None:
                self.cursor.execute(sql,args)
            else:
                self.cursor.execute(sql)
            self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
            print 'Mysql execute error'
            logs('------ '+ time.strftime("%Y-%m-%d %H-%M-%S")+' Mysql execute error: '+sql)
        return self.cursor


    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception, e:
            print e.message+'---cursor'
        try:
            if self.conn:
                self.conn.close()
        except Exception, e:
            print e.message+'===conn'

    def __del__(self):
        self.close()

# -*- coding: utf-8 -*-
# encoding: UTF-8

import urllib.request
import urllib.parse
import http.cookiejar
import random
import re
import json

class user:
    code = ''
    psw = ''
    def __init__(self,code,psw):
        self.code = code
        self.psw = psw


class poster:
    url = "http://moa.17u.cn"
    cookie = ""
    header = [("Accept-Encoding", "gzip,deflate"), ("Accept-Language", "zh-CN,en-US;q=0.8"), (
        "User-Agent",
        "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN"),
                              ("X-Requested-With", "com.tencent.mm")]
    data = []
    def excute(self,):
        assert self.data,'poster.data cannot be empty'
        post_date = urllib.parse.urlencode(self.data).encode('utf-8')
        if not self.cookie:
            self.cookie = http.cookiejar.CookieJar()

        openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))
        openner.addheaders = self.header
        r = openner.open(self.url, post_date)

        return r.read()

def veri(p:poster,u:user):
    print('\n获取验证码中。。。')
    p.data = [("mod", 'GetverificationCode'), ("employeeCode", u.code), ("employeePwd", u.psw), ("____v", random.random())]
    rCheck = p.excute().decode('utf-8')
    strRep = json.loads(rCheck)
    repHeader = strRep['responseHeader']
    strResult = repHeader['result']
    if strResult == "yes":
        print('\n获取成功')
    else:
        print('\n用户名或密码错误')
        exit()


def login(p:poster,u:user):
    checkCode = input("\n收到的验证码是:")
    print('\n正在登录中。。。')
    p.data = [("mod", 'onLogin'), ("employeeCode", u.code), ("employeePwd", u.psw),("checkcode",checkCode), ("____v", random.random())]
    rLogin = p.excute().decode('utf-8')
    strRep = json.loads(rLogin)
    repHeader = strRep['responseHeader']
    strResult = repHeader['result']
    if strResult == "ok":
        #TODO:设置cookie
        print('\n登陆成功')
    else:
        print('\n验证码不正确或已过期')
        exit()

def fetchData(p:poster):
    print('\n正在拉取加班数据。。。')
    p.data = [("mod", "onLoad"), ("pageIndex", "1"), ("StartTime", ""), ("EndTime",""), ("____v", random.random())]
    rOverTimes = p.excute().decode('utf-8')
    print('\n拉取加班数据成功')
    print('\n')
    print(rOverTimes)

    #过滤数据
    pattern = re.compile(r'<tr><td>[*]</td><td>[*]</td></tr>')
    s = pattern.findall(rOverTimes)
    print(s)


def start(u:user):

    p = poster()

    # 验证马
    veri(p,u)

    # 登录
    login(p,u)

    # 拉取加班数据
    fetchData(p)



if __name__ == '__main__':
    code = "12732"
    psw = "SKL12732"

    u = user(code,psw)
    start(u)
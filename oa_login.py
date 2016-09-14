import urllib.request
import urllib.parse
import http.cookiejar
import random
import json

class user:
    code = ''
    psw = ''
    def __init__(self,code,psw):
        self.code = code
        self.psw = psw

def post(data):
    url = ""

    post_date = urllib.parse.urlencode(data).encode('utf-8')
    cookie = http.cookiejar.CookieJar()
    openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    openner.addheaders = [("Accept-Encoding", "gzip,deflate"),("Accept-Language", "zh-CN,en-US;q=0.8"),("User-Agent","Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN"),("X-Requested-With","com.tencent.mm")]
    r = openner.open(url,post_date)

    print(r.read().decode('utf-8'))

def veri(u:user):
    dataVeri = [("mod", 'GetverificationCode'), ("employeeCode", u.code), ("employeePwd", u.psw), ("____v", random.random())]
    post(dataVeri)

def login(u:user,checkCode):
    dataLogin = [("mod", 'onLogin'), ("employeeCode", u.code), ("employeePwd", u.psw),("checkcode",checkCode), ("____v", random.random())]
    post(dataLogin)


if __name__ == '__main__':
    code = ""
    psw = ""

    u = user(code,psw)

 #   veri(u)
    login(u,'')
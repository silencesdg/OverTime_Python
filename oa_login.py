import urllib.request
import urllib.parse
import http.cookiejar

def post(code,psw):
	url = "http://moa.17u.cn"
	data = [("mod","GetverificationCode"),("employeeCode",code),("employeePwd",psw),("____v","0.3410145636950876")]
	post_date = urllib.parse.urlencode(data).encode('utf-8')
	# header = {"Accept-Encoding": "gzip,deflate","Accept-Language": "zh-CN,en-US;q=0.8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN","X-Requested-With": "com.tencent.mm"}
	cookie = http.cookiejar.CookieJar()
	openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
	openner.addheaders = [("Accept-Encoding", "gzip,deflate"),("Accept-Language", "zh-CN,en-US;q=0.8"),("User-Agent","Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN"),("X-Requested-With","com.tencent.mm")]
	r = openner.open(url,post_date)
	print(r.read().decode('utf-8'))

	# req = urllib.request.Request(url,post_date,header)
	# rep = urllib.request.urlopen(req)
	# print(rep)


if __name__ == '__main__':
	post("","")

import requests
import time
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "sso.telnet404.com",
    "Referer": "https://sso.telnet404.com/cas/login/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
}

#单点登录首页
BASE = 'https://sso.telnet404.com/cas/login'


URL_CAP = "https://sso.telnet404.com/captcha/"



#创建会话
session = requests.Session()

#get一下登录首页  在服务器端留下信息 使session生效 
base = session.get(BASE, headers=headers)

#获取到内容交给bs解析
base_c = base.content
bsObj = BeautifulSoup(base_c, 'lxml')

#找csfr信息  
csfr = bsObj.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

#验证码加上时间戳 保险
temp = '?t='+str(time.time()*100)[0:-6]

#获取验证码  二进制存储为pn
content = (session.get(URL_CAP+temp, headers=headers).content)

with open('./new.jpg','wb') as fp:
    fp.write(content)


print('请输入验证码')
captcha = input()

#构造请求数据
data = {
    'csrfmiddlewaretoken': csfr,
    'email': '18237010193@qq.com',
    'password': '132432532bug',
    'captcha': captcha,
}


#传送数据 进行登录操作
loginContext = session.post(BASE, headers=headers, data=data)

loginObj=BeautifulSoup(loginContext.content,'lxml')

# print(loginObj.find('title').get_text())
if loginObj.find('title').get_text()=='我的通行证 - Telnet 404':
    print('登录成功')
else:
    print('登录失败')
    return 


headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': 'www.seebug.org',
'Origin': 'https://www.seebug.org',
'Referer': 'https://www.seebug.org/vuldb/vulnerabilities',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'Cookie':'__jsluid_s=cdffa4b0544eccfc1144e6724c82bfe3; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1572914955; csrftoken=rywKM18vbmDKKDf0r9i53G0HyZYFOYhX; messages="6fe27ba169c9716377d3ce707a2e3d4d26f4dc61$[[\"__json_message\"\0540\05425\054\"Login succeeded. Welcome\054 53e541f98ac8.\"]\054[\"__json_message\"\0540\05425\054\"Login succeeded. Welcome\054 53e541f98ac8.\"]\054[\"__json_message\"\0540\05425\054\"Login succeeded. Welcome\054 53e541f98ac8.\"]\054[\"__json_message\"\0540\05425\054\"Login succeeded. Welcome\054 53e541f98ac8.\"]]"; sessionid=a7wchpvdh4uf47edoxrw01t98va389zm; Hm_lpvt_6b15558d6e6f640af728f65c4a5bf687=1572928563; __jsl_clearance=1572931015.852|0|hJJ8xYmulcs7DthmTdvhEHlJZNo%3D'
,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
# 这个csfr没啥用
loginCsfr=loginContext.headers.get('Set-Cookie').split(';')[0].split('=')[1]



page=session.get('https://www.seebug.org/vuldb/ssvid-98078',headers=headers)

# 详情页面 pageObj
pageObj=BeautifulSoup(page.content,'lxml')
print(pageObj.find('h1').get_text())
print(pageObj.find('section',{'class':'vul-basic-info'}))

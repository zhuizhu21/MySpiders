import requests,datetime
from bs4 import BeautifulSoup
s = requests.Session()

start=datetime.datetime.now()

URL = "https://yz.chsi.com.cn/user/?entrytype=yzgr"
Login = s.get(URL)

LoginOBJ = BeautifulSoup(Login.text, 'lxml').select(
    '#fm1 > div.yz-pc-loginbtn > input[type="hidden"]')

Id = LoginOBJ[0].get('value')

execution = LoginOBJ[1].get('value')


data = {
    'username': '填写用户名',
    'password': '填写密码',
    'submit': '登  录',
    'lt': Id,
    'execution':execution,
    '_eventId': 'submit'
}

URL="https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=https%3A%2F%2Fyz.chsi.com.cn%2Fj_spring_cas_security_check"

index=s.post(URL,data)

res=s.get('https://yz.chsi.com.cn/user/center.jsp')

infoOBJ=BeautifulSoup(res.text,'lxml')

info=infoOBJ.select('li.cxt3')

info=str(info[4])
print(info)
print('--------------------------------------------------\n')
if '未开通' in info:
    print('未开通')
else:
    print(info)
    print('--------------------------------------------------\n')
    url=BeautifulSoup(info,'lxml').find('a')
    url="https://yz.chsi.com.cn"+url.get('href')
    print(url)
    print('--------------------------------------------------\n')
    
    zkz=s.get(url)
    print(zkz.text)
    print('--------------------------------------------------\n')
    pdfPage=BeautifulSoup(zkz.text,'lxml')
    pdflist=pdfPage.find_all('a')
    for item in pdflist:
        text=item.get_text()
        if '下载' in text or '准考证' in text:
            print(item)
    
    

end=datetime.datetime.now()
print("运行耗时"+str(end-start).split(':')[2])

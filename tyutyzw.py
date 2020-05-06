import requests
from bs4 import BeautifulSoup

# 访问太原理工大学研招首页
URL_INFO="http://yz.tyut.edu.cn/sszs/fsdjlqzl.htm"
html=requests.get(URL_INFO)

# 修改响应编码
html.encoding = "UTF-8-SIG"
text=html.text.encode('utf-8')

bsObj=BeautifulSoup(text,'lxml')

#解析标签  获取特定的a标签和span标签  a标签为通知标题，span标签为时间
titleAll=bsObj.find_all('a',{'style':'TEXT-DECORATION: none; text-align:left;'})

timeAll=bsObj.find_all('span',{"style":"BACKGROUND-COLOR: #efefef"})

res=""
for i in range(len(titleAll)):
    title=titleAll[i].get_text()
    time=str(timeAll[i].get_text().encode()).split(' ')[1][-10:]
    # 获取第一条通知作为推送标题
    if i==0:
        info=time+' '+title
    res+='#### '+time+' '+title+'  \n'


# server酱消息推送
URL="https://sc.ftqq.com/SCU96652Tc0c696410a2ae2a2beb33f1bab3fbc815eb21b7f74246.send"

data={'text':info,'desp':res}
requests.post(URL,data=data)

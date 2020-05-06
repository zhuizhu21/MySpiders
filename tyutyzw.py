import requests,pandas
from bs4 import BeautifulSoup



URL_INFO="http://yz.tyut.edu.cn/sszs/fsdjlqzl.htm"

# res=pandas.read_html(URL_INFO)

# info=res[11]

# obj=info[0][1]

# obj.replace('·','')
# print(obj.split(' '))

# for item in info:
#     print(item)

# i=0
# for item in res:
#     print(i,end='=>            \t')
#     print(item)
#     i+=1

html=requests.get(URL_INFO)
html.encoding = "UTF-8-SIG"


text=html.text.encode('utf-8')

bsObj=BeautifulSoup(text,'lxml')


titleAll=bsObj.find_all('a',{'style':'TEXT-DECORATION: none; text-align:left;'})

timeAll=bsObj.find_all('span',{"style":"BACKGROUND-COLOR: #efefef"})

res=""
for i in range(len(titleAll)):
    title=titleAll[i].get_text()
    time=str(timeAll[i].get_text().encode()).split(' ')[1][-10:]
    res+=time+' '+title+'\n'

URL="https://sc.ftqq.com/SCU96652Tc0c696410a2ae2a2beb33f1bab3fbc815eb21b7f74246.send"

info="2020-05-05 关于公布2020年研招一志愿校内调剂审核结果的通知"
data={'text':info,'desp':res}
print(requests.post(URL,data=data))

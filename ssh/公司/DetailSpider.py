import requests
import time
import sqlite3
import threading
from threading import Lock
from selenium import webdriver
from bs4 import BeautifulSoup

#初始化数据库连接
conn = sqlite3.connect('./database/test.db')
cur = conn.cursor()

def getDetail(urlLIst,writeList):
    '''
    传入url，解析并写入数据库
    :param url: 
    :return: 
    '''
    for item in urlLIst:
        re=[]
        url=item[0]
        re.append(url)
        html = requests.get(url)
        # print(html.text)
        bsObj = BeautifulSoup(html.content, 'lxml')
        contentLIst = bsObj.find_all("td", {"class": "td-content"})
        num=0
        for it in contentLIst:
            num+=1
            if num==18:#截取18个必要元素 跳出循环 减小时间复杂度
                break
            if num==2:#字符串切分 公司名称会出现两次 截取第一个
                re.append(it.get_text().strip().split('&nbsp')[0])
            else:
                re.append(it.get_text().strip())
        writeList.append(re)
def readDatabase():
    #执行227次
    for i in range(227):
        print('page %d'%(i+1),end=" ")
        start=time.time()
        sql = "select * from urlset where not exists(select URL from detailset where urlset.url=detailset.URL)"
        cur.execute(sql)
        #cur.execute("select * from urlset limit " + str(i*100) + ",100")
        urlLIst = cur.fetchall()
        writeLIts = []
        t1=threading.Thread(target=getDetail,args=(urlLIst[0:25],writeLIts,))
        t2 = threading.Thread(target=getDetail, args=(urlLIst[25:50], writeLIts,))
        t3=threading.Thread(target=getDetail,args=(urlLIst[50:75],writeLIts,))
        t4 = threading.Thread(target=getDetail, args=(urlLIst[75:100], writeLIts,))
        t1.start()
        t1.join()
        t2.start()
        t2.join()
        t3.start()
        t3.join()
        t4.start()
        t4.join()
        for sI in writeLIts:
            try:
                cur.execute(
                    "insert into detailset values ('" + sI[0] + "','" + sI[2] + "','" + sI[2] + "','" +
                    sI[4] + "','" + sI[5] + "','" + sI[6] + "','" + sI[7] + "','" + sI[8] + "','" + sI[9] + "','" + sI[
                        10] + "','" + sI[11] + "','" + sI[12] + "','" + sI[13] + "','" + sI[14] + "','" + sI[
                        15] + "','" + sI[16] + "','" + sI[17] + "')")
            except:
                print('error')
                conn.commit()
        conn.commit()
        print("finished in %s seconds"%(time.time()-start))
    conn.close()
readDatabase()
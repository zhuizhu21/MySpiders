import requests
import time
import sqlite3
import threading
from threading import Lock
from selenium import webdriver
from bs4 import BeautifulSoup
#爬取详细信息是景太网页 直接requests来get，交给BS来解析

#初始化数据库连接
conn = sqlite3.connect('./database/test.db')
cur = conn.cursor()

def getDetail(urlLIst,writeList):
    '''
    入url，解析写入writeList
    :param urlLIst: 
    :param writeList: 
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
        for it in contentLIst:
            re.append(it.get_text())
        writeList.append(re)

def readDatabase():
    '''
    每次从数据库取出100条记录 分配给四个线程进行解析
    线程执行结束 将结果添加到传入的List参数 
    等待线程全部结束 对填充好的List进行迭代 存入数据库
    开四个线程 平均处理 1000条记录/12秒 根据网速和PC性能决定线程数
    :return: 
    '''
    for i in range(1):#
        print('page %d'%(i+1),end=" ")
        start=time.time()
        cur.execute("select * from urlset limit " + str(i*100) + ",100")
        #urlLIst = cur.fetchall()
        urlLIst=['http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000134837.html']
        writeList = []
        t1=threading.Thread(target=getDetail,args=(urlLIst[0:25],writeList,))
        t2 = threading.Thread(target=getDetail, args=(urlLIst[25:50], writeList,))
        t3=threading.Thread(target=getDetail,args=(urlLIst[50:75],writeList,))
        t4 = threading.Thread(target=getDetail, args=(urlLIst[75:100], writeList,))
        t1.start()
        t1.join()
        t2.start()
        t2.join()
        t3.start()
        t3.join()
        t4.start()
        t4.join()
        for sI in writeList:
            cur.execute(
                "insert into detailset values ('" + sI[0] + "','" + sI[1] + "','" + sI[2] + "','" + sI[3] + "','" +
                sI[4] + "','" + sI[5] + "','" + sI[6] + "','" + sI[7] + "','" + sI[8] + "','" + sI[9] + "','" + sI[
                    10] + "','" + sI[11] + "','" + sI[12] + "','" + sI[13] + "','" + sI[14] + "','" + sI[
                    15] + "','" + sI[16] + "','" + sI[17] + "')")
            try:
                pass
            except:
                print('error')
                conn.commit()
        conn.commit()
        print("finished in %s seconds"%(time.time()-start))
    conn.close()
readDatabase()
import requests
import time
import sqlite3
import threading
from selenium import webdriver
from bs4 import BeautifulSoup

#初始化数据库连接
conn = sqlite3.connect('./database/test.db')
cur = conn.cursor()

apiUrl="http://gs.amac.org.cn/amac-infodisc/api/pof/fund"

indexUrl="http://gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html"

#动态网页 使用无头浏览器模拟请求发方法
driver=webdriver.PhantomJS()

def getList():
    '''
    迭代获取页面中所有基金详细信息url
    :return: 
    '''
    base="http://gs.amac.org.cn/amac-infodisc/res/pof/fund/"
    driver.get(indexUrl)
    for i in range(5073):#爬取总页数
        print('正在爬取第'+str(i+1)+'/5073页')
        time.sleep(0.1)
        pagesource = driver.page_source
        #使用bs解析原网页文本
        bsObj = BeautifulSoup(pagesource, 'lxml')
        res = bsObj.find_all("a", {"class": "ajaxify"})

        for item in res:
            urlInfo=item.get('href')
            if '..' not in urlInfo:
                sqlToWrite = []
                newUrl=base+urlInfo
                print(newUrl)
                try:
                    cur.execute("insert into urlset values('"+newUrl+"')")
                except:
                    conn.commit()
        print('正在保存第' + str(i + 1) + '/5073页')
        conn.commit()
        try:
            driver.find_element_by_class_name('next').click()
        except:
            print("程序结束在第"+str(i+1)+"页")
    conn.close()
getList()
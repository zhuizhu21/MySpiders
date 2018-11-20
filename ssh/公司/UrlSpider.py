import requests
import time
import sqlite3
import threading
from selenium import webdriver
from bs4 import BeautifulSoup

#初始化数据库连接
conn = sqlite3.connect('./database/test.db')
cur = conn.cursor()

baseUrl="http://gs.amac.org.cn/amac-infodisc/res/pof/manager/"

indexUrl="http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html"


driver=webdriver.PhantomJS()


def getListNew():
    driver.get(indexUrl)
    #pages=1218
    for i in range(1218):
        start=time.time()
        print('saving page %d'%(i+1),end=" ")
        #需要获取渲染好的页面 根据网速设置延迟
        time.sleep(0.3)
        pagesource = driver.page_source
        # 使用bs解析原网页文本
        bsObj = BeautifulSoup(pagesource, 'lxml')
        aList = bsObj.find_all("a", {"target": "_blank"})
        for item in aList:
            url = item.get('href')
            if 'baidu' not in url:
                try:
                    cur.execute("insert into urlset values('" + baseUrl + url + "')")
                except:
                    print(baseUrl+url+"保存失败")
                    conn.commit()
        conn.commit()
        print("in %s seconds"%(time.time()-start))
        try:
            driver.find_element_by_class_name('next').click()
        except:
            print("程序结束在第" + str(i + 1) + "页")

getListNew()

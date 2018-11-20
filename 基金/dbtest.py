import sqlite3
#筛选未成功录入数据库的url
sql="select * from urlset where not exists(select URL from detailset where urlset.url=detailset.URL)"
conn=sqlite3.connect('./database/test.db')
cur=conn.cursor()
cur.execute(sql)
newlist=cur.fetchall()
for item in newlist:
    print(item[0])

'''
http status 404!
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000134837.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000142374.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000143117.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000194945.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000264180.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000347730.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000414214.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000414215.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000501788.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000567228.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000601764.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000603835.html
http://gs.amac.org.cn/amac-infodisc/res/pof/fund/351000756525.html
'''
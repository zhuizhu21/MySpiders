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
same
'''
# 爬虫
# 首先需要找到需要获取数据的页面
# 分析页面中哪些数据是我们需要的，找出数据的特征
# 导入网络请求库和html解析库
# 对目标网址发起请求，获取页面，根据数据特征，解析数据

# 目标页面  https://data.stats.gov.cn/search.htm?s=GDP

import requests
from bs4 import BeautifulSoup

URL="https://data.stats.gov.cn/search.htm?s=GDP&m=searchdata&db=&p=0"

session=requests.Session()

html=session.get(URL,verify=False)

resJson=html.json()

print("当前第%s页\t"%(resJson.get('pagecurrent')+1),"数据总量%s\t"%resJson.get('pagecount'))
resData=resJson.get('result')
# 指标	地区	数据时间	数值	所属栏目	相关报表    指标解释
for item in resData:
    item.pop('exp')
    print(item)
    # print(item.get('zb'),'\t',item.get('reg'),'\t',item.get('sj'),'\t',item.get('data').strip(),'\t',item.get('db').strip())


'''
当前第1页        数据总量200
{'data': '990865.1', 'db': '年度数据', 'prank': 1.7306409999999999, 'rank': 136.4, 'reg': '全国', 'report': 'cn=C01&zb=A0201&sj=2019', 'sj': '2019年', 'zb': '国内生产总值(亿元)'}
{'data': '919281.1', 'db': '年度数据', 'prank': 1.7306409999999999, 'rank': 136.4, 'reg': '全国', 'report': 'cn=C01&zb=A0201&sj=2018', 'sj': '2018年', 'zb': '国内生产总值(亿元)'}
{'data': '990865.1', 'db': '年度数据', 'prank': 1.7306409999999999, 'rank': 136.4, 'reg': '全国', 'report': 'cn=C01&zb=A0204&sj=2019', 'sj': '2019年', 'zb': '国内生产总值(亿元)'}
{'data': '919281.1', 'db': '年度数据', 'prank': 1.7306409999999999, 'rank': 136.4, 'reg': '全国', 'report': 'cn=C01&zb=A0204&sj=2018', 'sj': '2018年', 'zb': '国内生产总值(亿元)'}
{'data': '225495.5', 'db': '季度数据', 'prank': 1.731543, 'rank': 134.88, 'reg': '全国', 'report': 'cn=B01&zb=A0102&sj=2020B', 'sj': '2020年第二季度', 'zb': '国内生产总值(不变价)_当季值(亿元)'}
{'data': '409164.8', 'db': '季度数据', 'prank': 1.731543, 'rank': 134.88, 'reg': '全国', 'report': 'cn=B01&zb=A0102&sj=2020B', 'sj': '2020年第二季度', 'zb': '国内生产总值(不变价)_累计值(亿元)'}
{'data': '250110.1', 'db': '季度数据', 'prank': 1.731043, 'rank': 134.12, 'reg': '全国', 'report': 'cn=B01&zb=A0101&sj=2020B', 'sj': '2020年第二季度', 'zb': '国内生产总值_当季值(亿元)'}        
{'data': '456614.4', 'db': '季度数据', 'prank': 1.731043, 'rank': 134.12, 'reg': '全国', 'report': 'cn=B01&zb=A0101&sj=2020B', 'sj': '2020年第二季度', 'zb': '国内生产总值_累计值(亿元)'}        
{'data': '', 'db': '年度数据', 'prank': 1.7308409999999999, 'rank': 133.36, 'reg': '全国', 'report': 'cn=C01&zb=A0208&sj=2019', 'sj': '2019年', 'zb': '国内生产总值增长(百分点)'}
{'data': '6.7', 'db': '年度数据', 'prank': 1.7308409999999999, 'rank': 133.36, 'reg': '全国', 'report': 'cn=C01&zb=A0208&sj=2018', 'sj': '2018年', 'zb': '国内生产总值增长(百分点)'}
{'data': '11.5', 'db': '季度数据', 'prank': 1.731243, 'rank': 132.6, 'reg': '全国', 'report': 'cn=B01&zb=A0104&sj=2020B', 'sj': '2020年第二季度', 'zb': '国内生产总值环比增长速度(%)'}
{'data': '106.1', 'db': '年度数据', 'prank': 1.731641, 'rank': 132.6, 'reg': '全国', 'report': 'cn=C01&zb=A020201&sj=2019', 'sj': '2019年', 'zb': '国内生产总值指数(上年=100)'}
{'data': '106.7', 'db': '年度数据', 'prank': 1.731641, 'rank': 132.6, 'reg': '全国', 'report': 'cn=C01&zb=A020201&sj=2018', 'sj': '2018年', 'zb': '国内生产总值指数(上年=100)'}
{'data': '106.1', 'db': '年度数据', 'prank': 1.731641, 'rank': 132.6, 'reg': '全国', 'report': 'cn=C01&zb=A020501&sj=2019', 'sj': '2019年', 'zb': '国内生产总值指数(上年=100)'}
{'data': '106.7', 'db': '年度数据', 'prank': 1.731641, 'rank': 132.6, 'reg': '全国', 'report': 'cn=C01&zb=A020501&sj=2018', 'sj': '2018年', 'zb': '国内生产总值指数(上年=100)'}

'''

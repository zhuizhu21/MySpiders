>公司:
***
>>dir | database -> SQLite3数据库
>>file | datest.py -> 检索两张数据表不同的数据项
>>file | DetailSpider.py -> 读取数据库url，进行数据爬取，开了四个线程
>>file | UrlSpider.py -> 获取每个公司详细信息对应的url
>
***
>基金:
>>dir | database -> SQLite3数据库
>>file | datest.py -> 检索两张数据表不同的数据项
>>file | DetailSpider.py -> 读取数据库url，进行数据爬取，开了四个线程
>>file | UrlSpider.py -> 获取每只基金详细信息对应的url
>
***
>Tips:
>>多次测试，本地PC开四个线程、50M宽带环境下 100条数据的爬取与处理需要12秒，可以根据硬件与软件环境修改进程数.另外，SQLite3数据库对并发支持不是太好，在数据库选型方面，需要考虑。
>
***
# steamcommunity-market-price-forecaster
A tool which aims to obtain expection of price of item in steamcommunity market

# 一、爬虫
## 1. APPID
只要知道对应的 appid 和 hashname 即可查询任意物品的价格。
hashname的查询方法：在对应物品的网页右键查看源代码。ctrl+f 搜索 hash_name 即可。
然后
```
https://steamcommunity.com/market/pricehistory/?appid={{ appid }}&market_hash_name={{ hashname }}
```
prices里每一段代表一个节点。第一行代表时间；第二行是价格数据；第三行是交易数量；
如：
```
{"success":true,"price_prefix":"\u00a5","price_suffix":"","prices":[["Dec 11 2014 01: +0",2.524,"1249"],["Dec 12 2014 01: +0",0.785,"2116860"],["Dec 13 2014 01: +0",4.049,"11038"],["Dec 14 2014 01: +0",4.656,"149886"],["Dec 15 2014 01: +0",5.848,"147895"]}
```
## 2. 爬虫设置
爬虫中的header需要自己定制，一般找headers直接F12，转到networks，然后选第一个steamcommunity.com，找到User-Agent，Cookie这两项即可。
找到这两项之后，用笔记本打开headers.json，填到对应的地方。
爬虫会把抓取到的数据，以json格式储存在工作路径。
若欲更改保存的文件名字，只需要更改spider.py代码中的
```
filename = ''
```
若更改文件名，记得打开data.py一并修改。
## 3.使用
运行spider.py即可。
# 二、数据清洗
直接运行data.py即可。
steam提供的数据，最近一个月的数据频率是every hour，之前的数据则是every day。时间序列一般处理等时间间隔的数据比较合适，所以该程序会砍掉爬虫爬到的数据中最后一个月的数据，并保存为data.csv；之后，它会把爬虫爬到的数据全部保存为data_all.csv。

# 三、模型
模型部分使用R完成（尬笑），因为我不会用python做时间序列分析。在Rstudio中打开model.r即可。
利用autoarima函数直接获得ARIMA模型，如果不熟悉时间序列分析，请务必记住其反馈的ARIMA(p,i,q)中的p,q值。
之后进行ADF test和McLeod.Li test，检验通过后再套用GARCH模型。因为一般GARCH模型都是套用GARCH（1，1），我也就懒得再搞AIC和BIC了。
模型的最后一部分是作图，forecast30是ARIMA的图，forecast2是GARCH模型，最后一个plot则是把最后一个月被砍掉的数据呈现出来，以此进行对比。

# 其他
除了headers里面的cookie我删掉了，其他数据都是我爬的宝石数据。Rdata数据也一并留存，所有路径均为相对路径，只要在文件夹内打开一般路径都不会有问题。
有兴趣可以在此基础上改进一下，毕竟GARCH模型比较基础。
最后感谢keylol其乐论坛的帅疯疯的帮助，sff大佬(づ￣ 3￣)づ

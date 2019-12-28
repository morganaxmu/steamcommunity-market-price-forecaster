# steamcommunity-market-price-forcaster
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

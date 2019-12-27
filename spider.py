#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spider.py
#  
#  Copyright 2019 billy huang <billy huang@DESKTOP-77CQ0AV>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import requests 
import json
headers={
        'Host': 'steamcommunity.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': }
#headers直接F12，转到networks，然后选第一个steamcommunity.com
url= 'https://steamcommunity.com/market/pricehistory/?appid=753&market_hash_name=753-Sack of Gems' 
strhtml=requests.get(url,headers=headers,verify=False) 
content = json.loads(strhtml.text)
filename = 'Gems.json'
with open(filename,'w', encoding='utf-8') as name:
   name.write(str(content))

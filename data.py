#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data.py
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

import json
import csv
filename = 'Gems.json'
with open(filename) as f:
   data = f.read()
   data = eval(data)
   p_data = data['prices']
   times = []
   prices = []
   amouts = []
   for item in range(len(p_data)):
	   proxy = p_data[item]
	   times.append(proxy[0])
	   prices.append(proxy[1])
	   amouts.append(proxy[2])
filename1 = 'time.csv'
filename2 = 'price.csv'
filename3 = 'amout.csv'
with open(filename1, 'w', newline='') as cf1:
	csv1 = csv.writer(cf1)
	csv1.writerow(times)
with open(filename2, 'w', newline='') as cf2:
	csv1 = csv.writer(cf2)
	csv1.writerow(prices)
with open(filename3, 'w', newline='') as cf3:
	csv1 = csv.writer(cf3)
	csv1.writerow(amouts)
print("We now got the data!")

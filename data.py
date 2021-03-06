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
import numpy as np
filename = 'Gems.json'
with open(filename) as f:
   data = f.read()
   data = data.replace(': +0','')
   data = eval(data)
   p_data = data['prices']
   for item in range(len(p_data)-720):
	   proxy = p_data[item]
	   filename1 = 'data.csv'
	   with open(filename1, 'a', newline='') as cf1:
		   csv1 = csv.writer(cf1)
		   csv1.writerow(proxy)
for item in range(len(p_data)):
		proxy = p_data[item]
		filename2 = 'data_all.csv'
		with open(filename2, 'a', newline='') as cf2:
		   csv2 = csv.writer(cf2)
		   csv2.writerow(proxy)
print("We now got the data!")

# -*- coding: utf-8 -*-
import urllib
import psutil
import os
import time
import sys

i = 0
while i == 0:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 30.0:
			
			cpu = psutil.cpu_percent()
			os.system('netstat > net.html')
			scan = "net.html"
			lines = urllib.urlopen(scan).read()
			search = lines.find('coinhive')
			search1 = lines.find('rs-solution.de')
			search2 = lines.find('ns3033653.ip-164')
			search3 = lines.find('104.25.6.31')
			search4 = lines.find('104.24.104.76')
			search5 = lines.find('104.18.55.211')
			search6 = lines.find('104.27.185.32')
			search7 = lines.find('ns546545.ip-158-6')
			search8 = lines.find('beta00.cortacoin')
			search9 = lines.find('mail.aba.ae')
			search10 = lines.find('104.31.93.36')
			search11 = lines.find('104.31.92.36')
									
			if search != -1:
				print('Mining with Coinhive')
				
			elif search1 != -1:
				print('Mining with gustaver.ddns.net')
				
			elif search2 != -1:
				print('Mining with pon.ewtuyytdf45.com')
				
			elif search3 != -1:
				print('Mining with crypto-loot.com')
				
			elif search4 != -1:
				print('Mining with mepirtedic.com')
				
			elif search5 != -1:
				print('Mining with aster18cdn.nl')
				
			elif search6 != -1:
				print('Mining with cdn.whysoserius.club')
				
			elif search7 != -1:
				print('Mining with gtg02.bestsecurepractice.com')
				
			elif search8 != -1:
				print('Mining with beta00.cortacoin.com')
				
			elif search9 != -1:
				print('Mining with "mail.aba.ae" used by: freecontent.*, hashing.win, webassembly.stream, coinimp.com...')
				
			elif search10 != -1:
				print('Mining with crypto-loot.com')
				
			elif search11 != -1:
				print('Mining with crypta-loot.com')
				
			
									
			time.sleep( 10 )

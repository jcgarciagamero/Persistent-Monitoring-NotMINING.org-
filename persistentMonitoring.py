# -*- coding: utf-8 -*-
#Version: 2.0.0

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
			ip = (['coinhive','rs-solution.de','ns3033653.ip-164','104.25.6.31','104.24.104.76','104.18.55.211','104.27.185.32','ns546545.ip-158-6','beta00.cortacoin','mail.aba.ae',
			'104.31.93.36','104.31.92.36','ec2-52-57-80-78','5.255.86.116','45.77.196.10','45.63.109.36','207.246.116.117','45.77.192.104','188.166.33.242','178.62.227.52','104.18.46.158',
			'104.27.152.155','104.18.54.211','crypto-webminer','104.28.16.102','ns3083487.ip-145','ns3104461.ip-54','185.80.53.183','188.42.240.146','165.227.10.77','207.246.117.237',
			'206.189.24.193','104.28.15.29','192.99.34.204','212.32.255.7','212.32.255.210','35.184.61.56','45.32.172.211','144.202.45.243','207.246.77.212','104.20.66.187'])
			
			for busqueda in ip:
				search = lines.find(busqueda)	
				if search != -1:
					print("Miner Detected: " + busqueda)
					os.system('echo Miner Detected >> logs.txt')
					os.system('date >> logs.txt')
					break
			os.system('rm -rf net.html')			
			time.sleep( 10 )
			
				

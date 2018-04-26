# -*- coding: utf-8 -*-
import urllib
import psutil
import os
import time
import sys
from PyQt4 import QtGui  
from PyQt4.QtGui import QMessageBox  
aplicacion = QtGui.QApplication(sys.argv)


i = 0
while i == 0:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 40.0:
			
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
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search1 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gustaver.ddns.net',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search2 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with pon.ewtuyytdf45.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search3 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search4 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with mepirtedic.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search5 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with aster18cdn.nl',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search6 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with cdn.whysoserius.club',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search7 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gtg02.bestsecurepractice.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search8 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with beta00.cortacoin.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search9 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with "mail.aba.ae" used by: freecontent.*, hashing.win, webassembly.stream, coinimp.com...',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search10 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search11 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypta-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			
									
			time.sleep( 10 )

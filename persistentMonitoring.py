# -*- coding: utf-8 -*-

import psutil
import os
import time
import sys
from PyQt4 import QtGui  # importa el sub-módulo QtGui del módulo PyQt4
from PyQt4.QtGui import QMessageBox  # importa la clase QMessageBox del sub-módulo QtGui
aplicacion = QtGui.QApplication(sys.argv)

i = 0
while i == 0:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 40.0:
		cpu = psutil.cpu_percent()
		if cpu > 40.0:
			

			# abre una caja de mensaje informativo
			QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Suspect activity in your CPU. Is possible that you are visiting a infected website with cryptojacking',
                        QMessageBox.Ok,
                        QMessageBox.Ok)
			
			time.sleep( 10 )

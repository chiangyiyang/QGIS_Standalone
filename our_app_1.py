from qgis.core import *
from PyQt4.QtGui import *

from ourmainwindow_2 import OurMainWindow

app = QApplication([])
# set up QGIS
QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
QgsApplication.initQgis()

# set the main window and show it
mw = OurMainWindow()
mw.show()

app.exec_()

# "delete" our main window
mw = None
# clean up QGIS
QgsApplication.exitQgis()

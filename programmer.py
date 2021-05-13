# GUI import
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout , QLabel , QPushButton ,QWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore
# other import
from urllib.request import urlopen
import json
import pandas as pd
import random

# functions
from functions import frame1,frame2,frame3, frame4, grid



# initialize GUI application
app = QApplication(sys.argv)

# window and settings
window = QWidget()
window.setWindowTitle("Who wants to be a programmer ?")
window.setFixedWidth(1000)
window.move(800, 200)
window.setStyleSheet("background: #161219;")

# grid = QGridLayout()

# display frame 1
frame1()


window.setLayout(grid)

window.show()
sys.exit(app.exec()) # terminate the app
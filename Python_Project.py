# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class App():

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    
    def __init__(self):
            super().__init__()
            self.title = 'Chaos Game'
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 480
            self.initUI()
            
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
            
    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec_()
    
    button1 = QPushButton('Point 1')
    button1.clicked.connect(on_button_clicked)
    button1.show()
    
    button2 = QPushButton('Point 2')
    button2.clicked.connect(on_button_clicked)
    button2.show()
    
    button3 = QPushButton('Point 3')
    button3.clicked.connect(on_button_clicked)
    button3.show()
    
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    
    window.setLayout(layout)
    window.show()
    
if __name__ == "__main__":
    app.exec_()
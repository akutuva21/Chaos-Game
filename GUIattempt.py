from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt,QPoint
import sys,random,numpy

class  DrawPoint():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = QtCore.Qt.red

class  DrawBoard(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self,parent)
        self.setFixedSize(500, 400)
        self.vertexs = 3
        self.dataList = []
    
    def midpoint(self,p, q):
        return (0.5*(p[0] + q[0]), 0.5*(p[1] + q[1]))
    
    def drawCommon(self,numOfPoints,vertex,colors):
        N = numOfPoints
        currentPoint = DrawPoint()
        self.dataList.append(currentPoint)
        
        for i in range(1, N):
            k = random.randint(0, self.vertexs-1) # random triangle vertex
            currentPoint.x, currentPoint.y = self.midpoint((self.dataList[i-1][0],self.dataList[i-1][0]),(vertex[k][0],vertex[k][1]))
            currentPoint.color = colors[k]
            self.dataList.append(currentPoint)

    def drawTriAngle(self,numOfPoints):
        vertex = [(0, 0), (0.5, numpy.sqrt(3)/2), (1, 0)]
        colors = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.yellow]
        self.drawCommon(numOfPoints,vertex,colors)
        
       
    def drawRect(self,numOfPoints):
        vertex = [(0, 0),(1, 0),(0,1),(1.1)]
        colors = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.yellow,QtCore.Qt.blue]
        self.drawCommon(numOfPoints,vertex,colors)
    
    def drawPentagon(self,numOfPoints):
         N = numOfPoints
        
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawPoints(painter)
        painter.end()
       
    def drawPoints(self,painter):
        for i in self.dataList:
            painter.setPen(i.color)
            painter.drawPoint(i.x,i.y)
         
        
        
class ChaosGame(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup()
    def setup(self): 
        
        #add points
        self.points = QtWidgets.QComboBox(self)
        self.points.setObjectName("Points")
        self.points.addItem("100")
        self.points.addItem("500")
        self.points.addItem("1000")
        self.points.addItem("5000")
        self.points.addItem("8000")
        
        self.vertexs = QtWidgets.QComboBox(self)
        self.vertexs.setObjectName("Vertexs")
        self.vertexs.addItem("3")
        self.vertexs.addItem("4")
        self.vertexs.addItem("5")
        
        
        #add DrawBoard
        self.drawBoard = DrawBoard(self)
        
        #create play button
        self.playb = QtWidgets.QPushButton('Play', self)
        self.playb.setCheckable(True)
        #connect to slot
        self.playb.clicked.connect(self.on_play)
        pointLable = QtWidgets.QLabel("Points",self)
        vertexLable = QtWidgets.QLabel("Vertex",self)
        
        #grid layout
        self.grid = QtWidgets.QGridLayout() 
        self.grid.setSpacing(10)
        self.setLayout(self.grid) 
        self.grid.addWidget(pointLable, 1, 1) 
        self.grid.addWidget(self.points, 2, 1) 
        self.grid.addWidget(vertexLable, 3, 1)
        self.grid.addWidget(self.vertexs, 4, 1) 
        self.grid.addWidget(self.playb, 5, 1)
        self.grid.addWidget(self.drawBoard, 1, 2, 40, 40) 
        self.setWindowTitle('Chaos Game') 
        self.setGeometry(300, 300, 600, 600)
        self.show()
        
    def on_play(self):
        numOfPoint = int(str(self.points.currentText()))
        numOfVertex = int(str(self.vertexs.currentText()))
        
        if( numOfVertex == 5):
            self.drawBoard.drawPentagon(numOfPoint)
        elif( numOfVertex == 4):
            self.drawBoard.drawRect(numOfPoint)
        else:
            self.drawBoard.drawTriAngle(numOfPoint)
        
        
        self.repaint()
       
if __name__ == "__main__": 
   app = QtWidgets.QApplication(sys.argv)
   main_window = ChaosGame() 
   app.exec_()
        

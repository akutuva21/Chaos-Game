from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt,QPoint
import sys,random,numpy,math

# remaber color,x,y
class  DrawPoint():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = QtCore.Qt.red
#will draw on it 
class  DrawBoard(QtWidgets.QFrame):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self,parent)
        self.setFixedSize(420, 420)
        self.vertexs = 3
        self.N = 1000
        self.dataList = []
        self.verts = []
       
    def drawCommon(self,numOfPoints,numOfVertex,colors):
        
        self.N = numOfPoints
        self.vertex = numOfVertex
        
        sumX = 0
        sumY = 0
        #fr = 6.28/numOfVertex
        for i in range(0, numOfVertex):
            #angle = i*fr
            #x = 400*math.cos(angle)
            #y = 400*math.sin(angle)
            #vert = DrawPoint()
            #vert.x = x
            #vert.y = y
            #vert.color = colors[i]
            #verts.append(vert)
            sumX = sumX + self.verts[i].x()
            sumY = sumY + self.verts[i].y()
        
        seedX = sumX/numOfVertex
        seedY = sumY/numOfVertex
        
        currentPoint = DrawPoint()
        currentPoint.x, currentPoint.y = seedX,seedY
        
        numD = numOfVertex-1
        numM = numOfVertex-2
        
        for i in range(1, self.N):
            k = random.randint(0, numD) # random if use  possibility  need change
            currentPoint = DrawPoint()
            seedX = (seedX + numM*self.verts[k].x())/numD
            seedY = (seedY + numM*self.verts[k].y())/numD
            currentPoint.x, currentPoint.y = seedX,seedY
            currentPoint.color = colors[k]
            self.dataList.append(currentPoint)
            
   
    def drawTriAngle(self,numOfPoints):
        self.verts.append(QPoint(0,400))
        self.verts.append(QPoint(200,0))
        self.verts.append(QPoint(400,400))
        colors = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.yellow]
        self.drawCommon(numOfPoints,3,colors)
        
       
    def drawRect(self,numOfPoints):
        self.verts.append(QPoint(0,0))
        self.verts.append(QPoint(400,0))
        self.verts.append(QPoint(400,400))
        self.verts.append(QPoint(0,400))
        colors = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.yellow,QtCore.Qt.blue]
        self.drawCommon(numOfPoints,4,colors)
    
    def drawPentagon(self,numOfPoints):
        self.verts.append(QPoint(375,196))
        self.verts.append(QPoint(233,391))
        self.verts.append(QPoint(4,317))
        self.verts.append(QPoint(4,76))
        self.verts.append(QPoint(233,1))
        colors = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.yellow,QtCore.Qt.blue,QtCore.Qt.black]
        self.drawCommon(numOfPoints,5,colors)
        
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawPoints(painter)
        painter.end()
        
       
    def drawPoints(self,painter):
        if(self.verts):
            painter.setPen(QPen(Qt.darkBlue,  5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            poly = QtGui.QPolygon(self.verts)
            painter.drawPolygon(poly)
            self.verts = []
            
        for i in self.dataList:
            painter.setPen(QPen(i.color,5,Qt.SolidLine))
            painter.drawPoint(int(i.x),int(i.y))
        
        self.dataList = []
        
class ChaosGame(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self, parent) 
        self.setup() 
    def setup(self): 
        #add points
        self.points = QtWidgets.QComboBox(self)
        self.points.setObjectName("Points")
        self.points.addItem("500")
        self.points.addItem("1000")
        self.points.addItem("5000")
        self.points.addItem("8000")
        self.points.addItem("10000")
        self.points.addItem("20000")
        self.points.addItem("40000")
        
        self.vertexs = QtWidgets.QComboBox(self)
        self.vertexs.setObjectName("Vertexs")
        self.vertexs.addItem("3")
        self.vertexs.addItem("4")
        self.vertexs.addItem("5")
        
        
        #add DrawBoard
        self.drawBoard = DrawBoard(self)
        
        #create play button
        self.playb = QtWidgets.QPushButton('Draw', self)
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
        self.drawBoard.update()
        
class ChaosGameWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        self.setup()
    def setup(self):
        self.setWindowTitle("Chaos Game")
        self.setToolTip("Play Chaos Game") 
        self.game = ChaosGame(self) 
        self.setCentralWidget(self.game)
        self.setGeometry(300, 300, 600, 600)
        self.show()
       
if __name__ == "__main__": 
   app = QtWidgets.QApplication(sys.argv)
   main_window = ChaosGameWindow() 
   app.exec_()
        

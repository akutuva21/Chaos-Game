import sys, random, math
from PyQt5 import QtWidgets

import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class AppForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.create_main_frame()
        self.on_draw()

    def on_draw(self):
        def checkcolor(color):
            color = color.lower()
            if color == 'blue' or color == 'green' or color == 'red' or color == 'magenta' or color == 'yellow' or color == 'white':
                return list(color)[0]
            elif color == 'black':
                return 'k'
            else:
                checkcolor(input("Enter Another Color: "))

        i, ptlist, xvals, yvals = 0, [], [], []
        numiter = int(input("Enter The Number of Iterations: "))
        numsides = int(input("Enter The Number Of Sides (Not Too Many - Creates a Circle): "))
        while True:
            if numsides >= 3:
                break
            numsides = int(input("Try Again: "))
        color = checkcolor(input("Enter A Color: "))

        while True:
            if numsides >= 3 and type(numsides) == int:
                break
            numsides = input("Sorry, Wrong Input. Try again: ")

        rotation = int(input("Enter The Degrees of Rotation: "))
        while True:
            rotation %= 360
            if 0 <= rotation <= 360:
                break
            rotation = int(input("Sorry, Invalid Output. Try Again: "))
        rotation *= math.pi / 180  # https://en.wikipedia.org/wiki/Rotation_of_axes

        def pointfinder(N, n):
            # https://stackoverflow.com/questions/7198144/how-to-draw-a-n-sided-regular-polygon-in-cartesian-coordinates
            x = math.cos(2 * math.pi * n / N)
            y = math.sin(2 * math.pi * n / N)
            return (
            x * math.cos(rotation) + y * math.sin(rotation), -x * math.sin(rotation) + y * math.cos(rotation))

        for i in range(0, numsides):
            ptlist.append(pointfinder(numsides, i))

        def midpoint(x1, y1, x2, y2):
            return ((x2 + x1) / 2, (y2 + y1 / 2))

        r = random.randint(1, numsides)
        x = midpoint(ptlist[r - 1][0], ptlist[r - 1][0], ptlist[random.randint(0, numsides - 1)][0],
                     ptlist[random.randint(0, numsides - 1)][1])

        while i < numiter:
            r = random.randint(1, numsides)
            x = midpoint(x[0], x[1], ptlist[r - 1][0], ptlist[r - 1][1])
            xvals.append(x[0])
            yvals.append(x[1])
            i += 1

        #self.axes.tight_layout()
        self.axes.scatter(xvals, yvals, s=0.5, c=color, marker="o")
        self.canvas.draw()

    def create_main_frame(self):
        self.main_frame = QtWidgets.QWidget()
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_title('Chaos Game')
        self.axes.axis('off')
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()
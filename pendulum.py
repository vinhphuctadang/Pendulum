'''
Draw simple pendulum
'''

import log

import sys
from math import * 
from PySide2 import *
import time 

class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.limit = 100
        self.initUI()

        self.time = 0

        # w in wt+q
        self.w = 2*pi*(1/2) 

        # len of the rope
        self.l = 200 
        self.a0 = pi/3

        # time marker
        self.timePivot = time.time()

        # wt + q 
        # temporarily call it angle
        self.angle = -pi

        # center of the pendulum
        self.center = QtCore.QPoint(self.width()//2, self.height()//2)

    def getCurrentCoordinate(self):

        # compute the angle displayment
        a = self.a0 * cos(self.angle)

        position = QtCore.QPoint(
            self.center.x() - self.l*sin(a),
            self.center.y() - self.l*(1-cos(a))
        )

        return position 

    def initUI(self):
        self.text = u'Hello world'
        self.setGeometry(300, 200, 800, 600)
        self.setWindowTitle('Pendulum')
        self.show()

    # rotate the point q having pivot p
    def rotate(self, p, q):
        q = q * pi / 180
        return QtCore.QPoint(
            p.x()* cos(q) - p.y() * sin(q),
            p.x()* sin(q) + p.y() * cos(q)
        )

    def getDeltaTime(self):
        # get deltatime
        now = time.time()
        deltaTime = now - self.timePivot
        self.timePivot = now 
        return deltaTime

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(0xff, 0, 0))
        qp.setBrush(QtGui.QColor(0xff, 0xff, 0xff))
        
        # physic goes here
        deltaTime = self.getDeltaTime()

        w = self.w

        self.angle += deltaTime * w 
        self.angle -= (self.angle > 2*pi) * 2*pi 
        
        # render
        penCenter = self.getCurrentCoordinate()

        # draw the rope
        qp.drawLine(self.center.x(), self.center.y()-self.l, penCenter.x(), penCenter.y())

        # then draw the mass
        qp.drawEllipse(penCenter, 20, 20)
        
        qp.end()  
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()

    import threading 
    import time
    def updateUI(window):
        try: 
            while True:
                window.repaint()
                time.sleep(1/30)
        except KeyboardInterrupt:
            return 
    
    timer = threading.Timer(0.0, updateUI, [ex]) 
    timer.start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
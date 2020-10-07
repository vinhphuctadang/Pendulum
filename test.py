'''
Draw simple pendulum
'''

import log

import sys
from math import * 
from PySide2 import *

class Example(QtWidgets.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.limit = 100
        self.initUI()
        
    def initUI(self):      

        self.text = u'Hello world'

        self.setGeometry(300, 200, 800, 600)
        self.setWindowTitle('Draw text')
        self.show()

    def rotate(self, p, q):
        q = q * pi / 180
        return QtCore.QPoint(
            p.x()* cos(q) - p.y() * sin(q),
            p.x()* sin(q) + p.y() * cos(q)
        )

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        qp.setPen(QtGui.QColor(0xff, 0, 0))
        angle = 3.6
        p = QtCore.QPoint(self.width()//2, self.height()//2)
        qp.rotate(angle)
        for i in range(int(180/angle)):
            qp.rotate(angle * i)
            q = self.rotate(p, -angle*i)
            qp.drawEllipse(q, 200, 100)
            qp.rotate(-angle * i)
            
        qp.end()

        # angle = 3.6
        # p = QtCore.QPoint(self.width()//2, self.height()//2)
        # qp.rotate(angle)
        # q = self.rotate(p, -angle)
        # for i in range(self.limit):
        #     qp.rotate(angle)
        #     qp.drawEllipse(q, 200, 100)
        
    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)        
                
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()

    # import threading 
    # import time
    # def updateUI(window):
    #     try: 
    #         while True:
    #             window.limit += 1
    #             print(window.limit)
    #             window.repaint()
    #             time.sleep(0.2)
    #             if window.limit > 100:
    #                 window.limit = 0
    #     except KeyboardInterrupt:
    #         return 
    
    # timer = threading.Timer(0.0, updateUI, [ex]) 
    # timer.start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
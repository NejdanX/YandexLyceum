import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class BrushPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)


class Line:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:
    def __init__(self, cx, cy, x, y):
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, 2 * radius, 2 * radius)


class Canvas(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()

        self.objects = []
        self.instrument = 'Brush'

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        if self.instrument == 'Brush':
            self.objects.append(BrushPoint(event.x(), event.y()))
            self.update()
        elif self.instrument == 'Line':
            self.objects.append(Line(event.x(), event.y(), event.x(), event.y()))
            self.update()
        elif self.instrument == 'Circle':
            self.objects.append(Circle(event.x(), event.y(), event.x(), event.y()))
            self.update()

    def mouseMoveEvent(self, event):
        if self.instrument == 'Brush':
            self.objects.append(BrushPoint(event.x(), event.y()))
            self.update()
        elif self.instrument == 'Line':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'Circle':
            self.objects[-1].x = event.x()
            self.objects[-1].y = event.y()
            self.update()


    def setBrush(self):
        self.instrument = 'Brush'

    def setLine(self):
        self.instrument = 'Line'

    def setCircle(self):
        self.instrument = 'Circle'


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('paint.ui', self)

        self.setCentralWidget(Canvas())

        self.action_brush.triggered.connect(self.centralWidget().setBrush)
        self.action_line.triggered.connect(self.centralWidget().setLine)
        self.action_circle.triggered.connect(self.centralWidget().setCircle)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())

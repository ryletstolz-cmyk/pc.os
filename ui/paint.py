from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QPoint

class PaintApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint")
        self.resize(600, 400)
        self.last = QPoint()
        self.lines = []

    def mousePressEvent(self, e):
        self.last = e.pos()

    def mouseMoveEvent(self, e):
        self.lines.append((self.last, e.pos()))
        self.last = e.pos()
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setPen(QPen(Qt.white, 3))
        for l in self.lines:
            p.drawLine(*l)

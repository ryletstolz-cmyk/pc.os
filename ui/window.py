from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt, QPoint

class Window(QWidget):
    def __init__(self, title="Window"):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background:#2b2b2b; color:white;")

        self.drag_pos = QPoint()

        self.titlebar = QLabel(title, self)
        self.titlebar.setGeometry(0, 0, 300, 30)
        self.titlebar.setStyleSheet("background:#1e1e1e; padding-left:8px;")

        close = QPushButton("✕", self)
        close.setGeometry(270, 5, 20, 20)
        close.clicked.connect(self.close)

    def mousePressEvent(self, e):
        if e.y() < 30:
            self.drag_pos = e.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if not self.drag_pos.isNull():
            self.move(e.globalPos() - self.drag_pos)

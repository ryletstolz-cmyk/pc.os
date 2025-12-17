from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Qt

class Taskbar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, parent.height()-40, parent.width(), 40)
        self.setStyleSheet("background:#111;")

        start = QPushButton("Start", self)
        start.setGeometry(10, 5, 60, 30)

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt

def notify(parent, text):
    n = QLabel(text, parent)
    n.setStyleSheet("background:#333; color:white; padding:10px;")
    n.move(parent.width() - 220, parent.height() - 100)
    n.show()
    QTimer.singleShot(3000, n.close)

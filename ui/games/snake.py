from PySide6.QtWidgets import QWidget, QLabel

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake")
        QLabel("Snake coming soon ", self).move(20, 20)

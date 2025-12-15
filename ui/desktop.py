from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Qt
from ui.terminal import Terminal

class Desktop(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1e1e1e;")

        self.terminal = Terminal()

        terminal_icon = QPushButton("Terminal", self)
        terminal_icon.setGeometry(50, 50, 120, 40)
        terminal_icon.clicked.connect(self.open_terminal)

    def open_terminal(self):
        self.terminal.show()

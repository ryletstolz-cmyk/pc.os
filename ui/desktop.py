from PySide6.QtWidgets import QWidget, QPushButton
from ui.terminal import Terminal
from ui.files import FileExplorer
from ui.system import SystemInfo
from ui.gamers import GamersIO

class Desktop(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1e1e1e;")

        self.terminal = Terminal()
        self.files = FileExplorer()
        self.system = SystemInfo()
        self.gamers = GamersIO()

        self.icon("Terminal", 50, 50, self.terminal.show)
        self.icon("Files", 50, 110, self.files.show)
        self.icon("System", 50, 170, self.system.show)
        self.icon("gamers.io", 50, 230, self.gamers.show)

    def icon(self, text, x, y, action):
        btn = QPushButton(text, self)
        btn.setGeometry(x, y, 120, 40)
        btn.clicked.connect(action)


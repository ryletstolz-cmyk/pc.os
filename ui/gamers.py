from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from ui.games.snake import SnakeGame
from ui.games.clicker import ClickerGame

class GamersIO(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gamers.io")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select a Game"))

        btn1 = QPushButton("Clicker Quest")
        btn2 = QPushButton("Snake")

        btn1.clicked.connect(lambda: ClickerGame().show())
        btn2.clicked.connect(lambda: SnakeGame().show())

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

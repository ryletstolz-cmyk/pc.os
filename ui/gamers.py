from PySide6.QtWidgets import QPushButton, QVBoxLayout
from ui.window import Window
from ui.games.clicker import ClickerGame
from ui.games.snake import SnakeGame
from ui.games.tictactoe import TicTacToe
from ui.games.number_guess import NumberGuess

class GamersIO(Window):
    def __init__(self):
        super().__init__("gamers.io", 400, 350)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 40, 10, 10)

        layout.addWidget(self.launch("Clicker Quest", ClickerGame))
        layout.addWidget(self.launch("Snake", SnakeGame))
        layout.addWidget(self.launch("Tic Tac Toe", TicTacToe))
        layout.addWidget(self.launch("Number Guess", NumberGuess))

    def launch(self, name, game):
        btn = QPushButton(name)
        btn.clicked.connect(lambda: game().show())
        return btn

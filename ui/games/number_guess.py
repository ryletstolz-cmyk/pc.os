import random
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout

class NumberGuess(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Guess")
        self.num = random.randint(1, 10)

        self.label = QLabel("Guess a number 1–10")
        self.input = QLineEdit()
        self.input.returnPressed.connect(self.check)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.input)

    def check(self):
        guess = int(self.input.text())
        if guess == self.num:
            self.label.setText("Correct! 🎉")
        else:
            self.label.setText("Try again")

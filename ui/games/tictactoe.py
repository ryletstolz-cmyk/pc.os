from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.turn = "X"
        layout = QGridLayout(self)

        for i in range(3):
            for j in range(3):
                b = QPushButton("")
                b.setFixedSize(80, 80)
                b.clicked.connect(lambda _, btn=b: self.play(btn))
                layout.addWidget(b, i, j)

    def play(self, btn):
        if not btn.text():
            btn.setText(self.turn)
            self.turn = "O" if self.turn == "X" else "X"

from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

class GamersIO(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gamers.io")
        self.resize(400, 300)

        self.score = 0
        self.label = QLabel("Clicker Quest\n\nScore: 0")
        self.label.setStyleSheet("font-size: 18px;")

        self.button = QPushButton("CLICK ME")
        self.button.clicked.connect(self.click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def click(self):
        self.score += 1
        self.label.setText(f"Clicker Quest\n\nScore: {self.score}")

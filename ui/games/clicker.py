from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.label = QLabel("Score: 0")
        btn = QPushButton("Click")

        btn.clicked.connect(self.click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(btn)
        self.setLayout(layout)

    def click(self):
        self.score += 1
        self.label.setText(f"Score: {self.score}")

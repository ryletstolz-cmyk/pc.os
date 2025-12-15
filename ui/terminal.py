from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pcos Terminal")
        self.resize(600, 400)

        self.text = QTextEdit()
        self.text.setPlainText(
            "pcos terminal\n"
            "> help\n"
            "commands: help, version, status\n\n"
            "> version\n"
            "pcos 1.1\n"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)

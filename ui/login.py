from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        layout = QVBoxLayout()

        title = QLabel("pcos 1.1")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 32px;")

        self.user = QLineEdit()
        self.user.setPlaceholderText("Username")

        login = QPushButton("Login")
        login.clicked.connect(self.login)

        layout.addWidget(title)
        layout.addWidget(self.user)
        layout.addWidget(login)
        self.setLayout(layout)

    def login(self):
        self.stack.setCurrentIndex(2)

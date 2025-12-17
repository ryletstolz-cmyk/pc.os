from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class StartMenu(QWidget):
    def __init__(self, desktop):
        super().__init__(desktop)
        self.setFixedSize(200, 250)
        self.setStyleSheet("background:#222; color:white;")

        layout = QVBoxLayout(self)
        for name, app in desktop.apps.items():
            btn = QPushButton(name)
            btn.clicked.connect(app.show)
            layout.addWidget(btn)

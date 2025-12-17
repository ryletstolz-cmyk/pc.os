from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton
from ui.window import Window

class Settings(Window):
    def __init__(self):
        super().__init__("Settings", 400, 300)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 40, 10, 10)

        layout.addWidget(QLabel("pcos 1.1"))
        layout.addWidget(QLabel("A fun desktop OS simulator"))
        layout.addWidget(QLabel("Theme: Dark (default)"))

        btn = QPushButton("About pcos")
        btn.clicked.connect(self.about)

        layout.addWidget(btn)

    def about(self):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(
            self,
            "About",
            "pcos 1.1\nBuilt with Python + Qt\nFake OS, real fun 😄"
        )

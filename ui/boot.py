from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt

class BootScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setStyleSheet("background:black; color:white;")

        label = QLabel("pcos 1.1\n\nBooting system...")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:24px;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        QTimer.singleShot(2500, self.finish)

    def finish(self):
        self.stack.setCurrentIndex(1)

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt

class BootScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.setStyleSheet("background-color: black; color: white;")

        layout = QVBoxLayout()
        label = QLabel("pcos 1.1\n\nInitializing kernel...\nLoading desktop services...")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout.addWidget(label)
        self.setLayout(layout)

        QTimer.singleShot(3000, self.finish_boot)

    def finish_boot(self):
        self.stack.setCurrentIndex(1)

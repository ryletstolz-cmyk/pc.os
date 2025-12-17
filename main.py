import sys
from PySide6.QtWidgets import QApplication, QStackedWidget
from ui.boot import BootScreen
from ui.login import LoginScreen
from ui.desktop import Desktop

app = QApplication(sys.argv)

stack = QStackedWidget()

boot = BootScreen(stack)
login = LoginScreen(stack)
desktop = Desktop()

stack.addWidget(boot)     # index 0
stack.addWidget(login)    # index 1
stack.addWidget(desktop)  # index 2

stack.setCurrentWidget(boot)
stack.showFullScreen()

sys.exit(app.exec())

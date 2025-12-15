import sys
from PySide6.QtWidgets import QApplication, QStackedWidget
from ui.boot import BootScreen
from ui.desktop import Desktop

app = QApplication(sys.argv)

stack = QStackedWidget()

boot = BootScreen(stack)
desktop = Desktop()

stack.addWidget(boot)
stack.addWidget(desktop)

stack.setCurrentWidget(boot)
stack.showFullScreen()

sys.exit(app.exec())

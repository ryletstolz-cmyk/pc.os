from PySide6.QtWidgets import QLineEdit, QGridLayout, QPushButton
from ui.window import Window

class Calculator(Window):
    def __init__(self):
        super().__init__("Calculator", 250, 300)

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        layout = QGridLayout(self)
        layout.setContentsMargins(5, 35, 5, 5)
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, t=text: self.press(t))
            layout.addWidget(btn, 1 + i // 4, i % 4)

    def press(self, key):
        if key == "=":
            try:
                self.display.setText(str(eval(self.display.text())))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + key)

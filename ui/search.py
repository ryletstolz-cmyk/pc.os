from PySide6.QtWidgets import QWidget, QLineEdit, QListWidget, QVBoxLayout
from ui.fs import BASE_DIR

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search")
        self.resize(400, 300)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Search files...")
        self.input.textChanged.connect(self.search)

        self.results = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.results)
        self.setLayout(layout)

    def search(self, text):
        self.results.clear()
        if not text:
            return
        for p in BASE_DIR.rglob("*"):
            if text.lower() in p.name.lower():
                self.results.addItem(str(p.relative_to(BASE_DIR)))

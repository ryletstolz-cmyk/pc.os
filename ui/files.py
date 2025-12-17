from PySide6.QtWidgets import QListWidget, QVBoxLayout, QLabel, QMessageBox
from ui.window import Window
from ui.fs import init_fs

class FileExplorer(Window):
    def __init__(self):
        super().__init__("pcos Files", 500, 400)
        self.root = init_fs()
        self.current = self.root

        self.path = QLabel()
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.open)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 35, 5, 5)
        layout.addWidget(self.path)
        layout.addWidget(self.list)

        self.refresh()

    def refresh(self):
        self.list.clear()
        self.path.setText(str(self.current))

        if self.current != self.root:
            self.list.addItem("..")

        for p in self.current.iterdir():
            self.list.addItem(p.name)

    def open(self, item):
        name = item.text()
        if name == "..":
            self.current = self.current.parent
        else:
            path = self.current / name
            if path.is_dir():
                self.current = path
            else:
                QMessageBox.information(self, "File", path.read_text(errors="ignore"))
        self.refresh()



from PySide6.QtWidgets import (
    QWidget, QListWidget, QVBoxLayout, QLabel, QMessageBox
)
from pathlib import Path
from ui.fs import init_fs

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pcos Files")
        self.resize(500, 400)

        self.root = init_fs()
        self.current = self.root

        self.path_label = QLabel(str(self.current))
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.open_item)

        layout = QVBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(self.list)
        self.setLayout(layout)

        self.refresh()

    def refresh(self):
        self.list.clear()
        self.path_label.setText(str(self.current))

        if self.current != self.root:
            self.list.addItem("..")

        for item in self.current.iterdir():
            self.list.addItem(item.name)

    def open_item(self, item):
        name = item.text()

        if name == "..":
            self.current = self.current.parent
        else:
            path = self.current / name
            if path.is_dir():
                self.current = path
            else:
                QMessageBox.information(
                    self,
                    "File",
                    path.read_text(errors="ignore")
                )
        self.refresh()

from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QPushButton, QFileDialog
from ui.window import Window
from ui.fs import BASE_DIR

class Notepad(Window):
    def __init__(self):
        super().__init__("Notepad", 600, 400)

        self.editor = QTextEdit()

        save = QPushButton("Save")
        save.clicked.connect(self.save)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 35, 5, 5)
        layout.addWidget(self.editor)
        layout.addWidget(save)

    def save(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            str(BASE_DIR),
            "Text Files (*.txt)"
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())

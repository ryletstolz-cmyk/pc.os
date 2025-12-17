from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QLineEdit
from ui.fs import BASE_DIR

class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pcos Terminal")
        self.resize(600, 400)

        self.cwd = BASE_DIR

        self.out = QTextEdit(readOnly=True)
        self.inp = QLineEdit()
        self.inp.returnPressed.connect(self.run)

        layout = QVBoxLayout()
        layout.addWidget(self.out)
        layout.addWidget(self.inp)
        self.setLayout(layout)

        self.print(f"pcos terminal\n{self.cwd}")

    def print(self, txt):
        self.out.append(txt)

    def run(self):
        cmd = self.inp.text().strip()
        self.inp.clear()
        self.print(f"> {cmd}")

        parts = cmd.split()
        if not parts:
            return

        c = parts[0]

        if c == "ls":
            self.print("\n".join(p.name for p in self.cwd.iterdir()))
        elif c == "cd" and len(parts) > 1:
            path = (self.cwd / parts[1]).resolve()
            if BASE_DIR in path.parents or path == BASE_DIR:
                self.cwd = path
            self.print(str(self.cwd))
        elif c == "cat" and len(parts) > 1:
            file = self.cwd / parts[1]
            self.print(file.read_text(errors="ignore"))
        elif c == "clear":
            self.out.clear()
        elif c == "reboot":
            self.print("Rebooting... (fake)")
        else:
            self.print("Unknown command")

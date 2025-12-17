from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QLineEdit
from ui.window import Window
from ui.fs import BASE_DIR

class Terminal(Window):
    def __init__(self):
        super().__init__("pcos Terminal", 600, 400)
        self.cwd = BASE_DIR

        self.out = QTextEdit(readOnly=True)
        self.inp = QLineEdit()
        self.inp.returnPressed.connect(self.run)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 35, 5, 5)
        layout.addWidget(self.out)
        layout.addWidget(self.inp)

        self.out.append(f"pcos terminal\n{self.cwd}")

    def run(self):
        cmd = self.inp.text().strip()
        self.inp.clear()
        self.out.append(f"> {cmd}")

        if cmd == "ls":
            self.out.append("\n".join(p.name for p in self.cwd.iterdir()))
        elif cmd.startswith("cd "):
            target = self.cwd / cmd[3:]
            if target.exists():
                self.cwd = target
                self.out.append(str(self.cwd))
        elif cmd == "clear":
            self.out.clear()
        else:
            self.out.append("Unknown command")

        elif c == "reboot":
            self.print("Rebooting... (fake)")
        else:
            self.print("Unknown command")

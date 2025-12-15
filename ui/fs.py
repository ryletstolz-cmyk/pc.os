from pathlib import Path

BASE_DIR = Path.home() / "pcos_home"

def init_fs():
    (BASE_DIR / "Documents").mkdir(parents=True, exist_ok=True)
    (BASE_DIR / "Games").mkdir(exist_ok=True)

    readme = BASE_DIR / "readme.txt"
    if not readme.exists():
        readme.write_text(
            "Welcome to pcos 1.1\n\n"
            "This is your home directory.\n"
            "Check out Games/ for gamers.io titles."
        )

    return BASE_DIR

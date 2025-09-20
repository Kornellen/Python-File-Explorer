from pathlib import Path
from modules import Window, Colors

ignored_dirs = [
    "node_modules",
    "__pycache__",
    "venv",
    "env",
    ".git",
    ".vscode",
    ".vs",
    ".idea",
    "migrations",
    "bin",
    "obj",
    "build",
]


def getFiles(
    tree, parent, path: Path, window: Window, depth: int = 0, is_logging_on: bool = True
) -> None:
    indent = "  " * depth
    for item in path.iterdir():
        if item.is_dir() and item.name not in ignored_dirs:
            node = window.AddComponent(parent, f"{indent}📁 {item.name}/")
            (
                print(
                    f"{Colors.dir_color}{indent}📁 {item.name}/{Colors.default_color}"
                )
                if is_logging_on
                else ""
            )
            getFiles(tree, node, item, window, depth + 1, is_logging_on)
        else:
            is_dir = "/" if item.is_dir() else ""
            icon = "📁" if is_dir else "📄"
            (
                print(
                    f"{Colors.dir_color if is_dir else ""}{indent}{icon} {item.name}{is_dir}{Colors.default_color}"
                )
                if is_logging_on
                else ""
            )
            window.AddComponent(parent, f"{indent}{icon} {item.name}{is_dir}")

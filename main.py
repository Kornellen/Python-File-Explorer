from pathlib import Path
from dotenv import dotenv_values
from modules import Window, getFiles

env_path = dotenv_values("./.env")["PATH"]


def main() -> None:
    try:
        window = Window("Project Strucutrer", 100)
        if env_path:
            path = Path(env_path)

            root_tree = window.tree.insert("", "end", text=f"📁 {path}", open=True)

            getFiles(window.tree, root_tree, path, window, is_logging_on=False)
            window.Run()
        else:
            raise ValueError("PATH variable is not setted up")

    except ValueError as value_err:
        print(value_err)

    except KeyboardInterrupt:
        print("User stopped program")

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

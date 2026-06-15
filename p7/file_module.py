import os
FILES_DIR = "saved_files"


def _get_path(filename):
    """Build full path and make sure the folder exists."""
    os.makedirs(FILES_DIR, exist_ok=True)
    return os.path.join(FILES_DIR, filename)


def create_file():
    filename = input("Enter file name: ").strip()

    if "." not in filename:
        filename += ".txt"

    path = _get_path(filename)

    if os.path.exists(path):
        print(f"File '{filename}' already exists!")
    else:
        with open(path, "w") as f:
            pass
        print("File created successfully!")


def write_file():
    filename = input("Enter file name: ").strip()

    if "." not in filename:
        filename += ".txt"
    path = _get_path(filename)
    data = input("Enter data to write: ")
    with open(path, "w") as f:
        f.write(data + "\n")
    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ").strip()

    if "." not in filename:
        filename += ".txt"
    path = _get_path(filename)
    if not os.path.exists(path):
        print(f"File '{filename}' not found!")
    else:
        with open(path, "r") as f:
            content = f.read()
        print("File Content:")
        print(content)


def append_file():
    filename = input("Enter file name: ").strip()

    if "." not in filename:
        filename += ".txt"
    path = _get_path(filename)
    if not os.path.exists(path):
        print(f"File '{filename}' not found! Create it first.")
    else:
        data = input("Enter data to append: ")
        with open(path, "a") as f:
            f.write(data + "\n")
        print("Data appended successfully!")



if __name__ == "__main__":
    create_file()

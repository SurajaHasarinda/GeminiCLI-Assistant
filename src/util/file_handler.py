import os

def list_files_and_folders(directory="."):
    """Lists only the files and folders in the specified directory."""
    try:
        return os.popen('dir').read().splitlines()  # 'ls' for Unix-based systems | 'dir' for Windows
    except FileNotFoundError:
        return [f"⚠️ Error: Directory '{directory}' not found."]
    except PermissionError:
        return [f"⚠️ Error: No permission to access '{directory}'."]
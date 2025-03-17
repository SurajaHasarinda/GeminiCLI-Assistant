import os
import difflib

def list_files_and_folders(directory="."):
    """Lists only the files and folders in the specified directory."""
    try:
        return os.popen('dir').read().splitlines()  # 'ls' for Unix-based systems | 'dir' for Windows
    except FileNotFoundError:
        return [f"⚠️ Error: Directory '{directory}' not found."]
    except PermissionError:
        return [f"⚠️ Error: No permission to access '{directory}'."]

def find_closest_filename(directory, target_filename):
    """Finds the closest matching filename in the given directory."""
    try:
        files = os.listdir(directory)
        matches = difflib.get_close_matches(target_filename, files, n=1, cutoff=0.6)  # Adjust cutoff as needed
        
        return matches[0] if matches else None  # Return closest match or None if no match found
    except Exception as e:
        return f"Error: {e}"
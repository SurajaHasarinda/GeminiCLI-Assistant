import subprocess

def get_git_status():
    """Fetch the staged changes from the Git status."""
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    status_output = result.stdout.strip()

    # Find the start and end of the "Changes to be committed" section
    start_index = status_output.find("Changes to be committed:")
    end_index = status_output.find("Changes not staged for commit:")

    # If no staged changes, return None
    if start_index == -1:
        return None
    
    staged_changes = status_output[start_index:end_index].strip()
    return staged_changes

def get_git_staged_files():
    """Fetch the list of staged files in Git."""
    result = subprocess.run(["git", "diff", "--name-only", "--cached"], capture_output=True, text=True)
    return result.stdout.strip().split("\n")
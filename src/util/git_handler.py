import subprocess

def run_git_command(command):
    """Execute a Git command and handle errors gracefully."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing {' '.join(command)}:\n{e.stderr.strip()}")
        return None

def get_git_status():
    """Fetch the staged changes from the Git status."""
    status_output = run_git_command(["git", "status"])
    if not status_output:
        return None

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
    return run_git_command(["git", "diff", "--name-only", "--cached"]).split("\n")

def commit_changes(message):
    """Commits changes with a given message."""
    return run_git_command(["git", "commit", "-m", message])
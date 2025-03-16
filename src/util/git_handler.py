import subprocess

def get_git_diff():
    """Fetch the latest Git diff."""
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    return result.stdout.strip()

def get_git_status():
    """Fetch the current Git status."""
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    return result.stdout.strip()
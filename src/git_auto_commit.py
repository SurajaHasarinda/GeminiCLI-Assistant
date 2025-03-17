from util.git_handler import get_git_status
from util.gemini import model
import subprocess

def generate_commit_message(status):
    """Use Gemini AI to generate a concise and professional commit message based on the status."""
    if not status:
        return "No changes detected to commit."

    prompt = f"""
    * Generate a concise and professional Git commit message following this structure:
        add: <scope>
        modify: <scope>
        remove: <scope>
        refactor: <scope>

    Constraints:
    * Only include the commit message in the response.
    * Include the affected file names in <scope>.
    * Use 'add' for new files, 'modify' for changes, 'remove' for deletions, and 'refactor' for refactoring.
    * Do not include any additional details or explanations.

    Changes:
    {status}
    """
    response = model.generate_content(prompt)

    return response.text.strip() if response.text else "Commit changes."

def git_auto_commit():
    git_status = get_git_status()
    if not git_status:
        print("⚠️ No staged changes found.")
        return

    commit_message = generate_commit_message(git_status)
    print("\n✅ Suggested Commit Message:")
    print(f"🔹 {commit_message}")

    confirm = input("\nDo you want to commit this change? ('y' to commit, 'n' to abort, 'c' to customize): ").strip().lower()

    if confirm == "y":
        subprocess.run(["git", "commit", "-m", commit_message])
        print("✅ Commit successful!")
    elif confirm == "c":
        custom_message = input("Enter a custom commit message (or type 'n' to cancel): ").strip()
        if custom_message != "n":
            subprocess.run(["git", "commit", "-m", custom_message])
            print("✅ Commit successful!")
        else:
            print("🚫 Commit aborted")
    elif confirm == "n":
        print("🚫 Commit aborted")
    else:
        print("⚠️ Invalid input. Please enter 'y', 'n', or 'c'. Commit aborted.")

if __name__ == "__main__":
    git_auto_commit()
from util.git_handler import get_git_status
from util.gemini import model
import subprocess

def generate_commit_message(status):
    """Use Gemini AI to generate a concise and professional commit message based on the status."""
    if not status:
        return "No changes detected to commit."

    prompt = f"""
    Generate a concise and professional Git commit message following this structure:

    <type>(<scope>): <subject> 

    - Identify the appropriate commit type (feat, fix, docs, style, refactor, test, chore).
    - Include the affected file names in <scope>.
    - Provide a brief summary of the changes in <subject>.
    - Do this to each file with changes.

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

    confirm = input("\nDo you want to commit this change? (y/N): ").strip().lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", commit_message])

if __name__ == "__main__":
    git_auto_commit()
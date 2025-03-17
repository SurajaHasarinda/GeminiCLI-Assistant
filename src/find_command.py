from util.file_handler import list_files_and_folders
from util.command_executor import execute_command
from util.gemini import model

def ask_gemini_command(query, directory="."):
    """Ask Gemini AI for a command based on a description and available files/folders."""
    try:
        files_folders = "\n".join(list_files_and_folders(directory)) or "No files or folders found."
        prompt = f"""
        Based on the following files and folders in the current directory:
        {files_folders}

        * Provide only the necessary command (in the simplest form) to achieve the following:
        {query}

        Constraints:
        * Command should support command-line interface (CLI) syntax.
        * Do not include any explanations, context, or surrounding code blocks (no "```shell...```").
        * Only provide the command for existing files and folders unless creating new ones (Generate names base on the query).
        """
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "⚠️ No response received."
    except Exception as e:
        return f"⚠️ Error: {e}"

def find_command():
    print("\n💡 AI Assistant - Ask Gemini for a Command! 💡")
    while True:
        query = input("\n🔹 Enter a command description (or type 'q' to quit): ").strip()
        if query.lower() == "q":
            print("👋 Exiting...")
            break

        command = ask_gemini_command(query)
        print("\n✅ Gemini's Suggested Command:")
        print(f"🔹 {command}")

        execute_command(command)
    
if __name__ == "__main__":
    find_command()
from util.file_handler import list_files_and_folders, find_closest_filename
from util.gemini import model
from util.command_executor import execute_command, filter_commands
import subprocess

def get_gemini_command(directory="."):
    """Ask Gemini AI to generate CLI commands for organizing files into folders by type."""

    files_folders = "\n".join(list_files_and_folders(directory)) or "No files or folders found."
    
    try:
        prompt = f"""
        You are an expert file organizer. Given the following list of files and folders in the current directory:

        {files_folders}

        Your task is to generate a series of shell commands to organize these files into folders based on their file extensions. Follow these rules precisely:

        Folder Creation:
        * Create a folder only if it does not already exist.
        * Create each folder only once.
        * Only create folders necessary for the files provided.
        * Folder names must match the file type categories below.

        File Movement:
        * Move each file to the appropriate folder based on its extension.
        * Use the exact file name, including the extension, enclosed in double quotes.
        * Do not modify file names or extensions.

        Folder Categories:
        * `Documents`: For ".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx" files.
        * `Pictures`: For ".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp" files.
        * `Videos`: For ".mp4", ".avi", ".mov", ".mkv" files.
        * `Audio`: For ".mp3", ".wav", ".flac", ".ogg" files.
        * `Programs`: For ".exe", ".dmg", ".app", ".msi" files.
        * `Games`: For ".gam", ".gme", ".install" files.
        * `Archives`: For ".zip", ".rar", ".tar", ".gz", ".7z" files.
        * `Code`: For ".py", ".js", ".java", ".cpp", ".c", ".html", ".css" files.
        * `Data`: For ".json", ".xml", ".csv", ".db", ".sql" files.
        * `Backups`: For ".bak", ".backup", ".save" files.
        * `Research`: For ".research", ".study" files.
        * `Notes`: For ".note", ".memo" files.
        * `Trash`: For ".tmp", ".delete" files.

        Output Format:
        * Provide only raw shell commands.
        * Do not include any explanations, context, or surrounding code blocks (no "```shell...```").
        * Use the following command structure:
            * `mkdir <folder>` (only if the folder does not exist)
            * `move "<file>" <folder>`

        Constraints:
        * Process only the files listed in the input.
        * Do not assume the existence of any other files.
        * Ignore subdirectories; only organize files in the current directory.
        """

        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "⚠️ No response received."
    
    except Exception as e:
        return f"⚠️ Error: {e}"

def sort_files():
    confirm = input("\n⚡ Do you want to sort the directory? (y/n): ").strip().lower()
    if confirm == "y":
        print("🗃️🔀 Sorting directory...")
        commands = get_gemini_command()
        valid_commands = filter_commands(commands, ["mkdir", "move"], directory=".").splitlines()  # 'move' for Windows | 'mv' for Unix-based systems

        if not valid_commands:
            print("⚠️ No file sorting commands generated.")
        else:
            for command in valid_commands:
                try:
                    # Run the move command silently
                    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"✅ Executed: {command}")
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Error executing command: {command}")
                    print(f"Details: {e}")
    else:
        print("❌ Directory sorting canceled.")
        return

if __name__ == "__main__":
    sort_files()

def show_help(batch_file_name):
    help_text = f"""
    =======================================
        🤖  CLI Assistant - Help Guide   
    =======================================
    This assistant helps automate common tasks using AI-powered scripts.
    
    Available commands:
      {batch_file_name} help        - Display this help information
      {batch_file_name} findcmd     - Find a command based on a natural language description
      {batch_file_name} autocommit  - Automate Git commits with a single command
      {batch_file_name} sortfiles   - Sort files and folders in the current directory
      {batch_file_name} chat        - Start an interactive chat with Gemini AI
    
    Usage:
      {batch_file_name} <command> [args]
    =======================================
    """
    print(help_text)

if __name__ == "__main__":
    show_help("ai") # 'ai' is the default batch file name

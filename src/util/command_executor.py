import os

def execute_command(command):
    """Executes the given command after confirmation."""
    confirm = input("\n⚡ Do you want to execute this command? (y/N): ").strip().lower()
    if confirm == "y":
        try:
            os.system(command)
        except Exception as e:
            print(f"⚠️ Error executing command: {e}")
    else:
        print("❌ Command execution canceled.")

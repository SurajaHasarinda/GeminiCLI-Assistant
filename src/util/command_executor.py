import os
import shlex
from util.file_handler import find_closest_filename

def execute_command(command):
    """Executes the given command after confirmation."""
    confirm = input("\n⚡ Do you want to execute this command? (y/n): ").strip().lower()
    if confirm == "y":
        try:
            os.system(command)
            print(f"✅ Executed command: {command}")
        except Exception as e:
            print(f"⚠️ Error executing command: {e}")
    else:
        print("❌ Command execution canceled.")

def filter_commands(commands, allowed_commands, directory, file_name_checker=True):
    """Filters out commands that are not in the allowed commands list and checks for correct file names."""
    
    command_list = commands.splitlines()
    valid_commands = []
    
    for cmd in command_list:
        if cmd:
            # Use shlex.split() to handle quoted file names correctly
            try:
                parts = shlex.split(cmd)
            except ValueError as e:
                print(f"Skipping invalid command: {cmd} (Error: {e})")
                continue
            
            # Check if command is in allowed commands
            if parts and parts[0] in allowed_commands:
                
                # Extract file name from the command
                if file_name_checker and len(parts) > 1:
                    file_name = parts[1]  # The second part is the file name
                    
                    # If a file name is found, attempt to find the closest match
                    closest_match = find_closest_filename(directory, file_name)
                    if closest_match and closest_match != file_name:
                        # Replace the incorrect file name with the closest match
                        parts[1] = closest_match
                        cmd = " ".join([parts[0]] + [f'"{part}"' if " " in part else part for part in parts[1:]])
                
                valid_commands.append(cmd)
    
    return "\n".join(valid_commands)
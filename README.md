# GeminiCLI-Assistant 🤖

## Overview 📌🔍💡

### Description 📝📜📚
**GeminiCLI-Assistant** is a command-line AI assistant powered by Google Gemini AI. It helps users generate and execute shell commands based on natural language descriptions. The assistant can also automate Git and other CLI tasks efficiently. 🤖🖥️⚡

### Workflow 🔄🔁📊
![workflow](/assest/screenshot-1.png)

## Features 🔥🔧🛠️
- Convert natural language descriptions into CLI commands 🎙️💬🖥️
- Execute generated commands interactively 🚀✅🖱️
- List files and folders for contextual command suggestions 📁📂🔎
- Automate Git commits with a single command 📝🔄✅
- Works on Windows Command Prompt 🏁💻🖱️

## Setup and Installation 🔧📥🖥️
### Prerequisites ⚙️🔎✅
- Python 3.8+ 🐍🖥️📦
- Pip 📦🔄✅
- Google Gemini API Key 🔑🔐📜 (saved in `.env` file)

### Installation Steps 📌📂🛠️
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/GeminiCLI-Assistant.git
   cd GeminiCLI-Assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the `.env` file:
- Create a new file named `.env` in the project root directory and add the following lines:

   ```sh
   GEMINI_API_KEY=your-api-key-here
   GEMINI_MODEL=your-model-id-here # e.g. - "gemini-2.0-flash"
   ```

### Setting up environment variables in Windows 🖥️🔧📂
1. Search for "Environment Variables" in the Windows search bar.
2. Click on "Environment Variables" in the System Properties window.
3. Under "System Variables," select "Path" and click "Edit."
4. Add the path of the `.bat` (ai.bat) file to the list of paths.

### Get Google Gemini API Key 🔑🔐📜
1. Visit the [Google Gemini API page](https://ai.google.dev/gemini-api/docs)
2. Sign in with your Google account.
3. Click on the "Get a Gemini API Key" button.
4. Generate a new API key and copy it.

### Available Commands 🎯🎙️💬
- `ai help` - Display help information about the assistant
- `ai findcmd` - Find a command based on a natural language description
- `ai autocommit` - Automate Git commits with a single 
- `ai sortfiles` - Sort files and folders in the current directory

**The `ai` command can be customized by renaming the `ai.bat` file in the project root directory.**

## License 📜🔓✅
This project is licensed under the MIT License. ⚖️📖✅

## Contribution 🚀📬🤝
Feel free to submit issues and pull requests to improve the project! 🛠️📢🚀

---
**Author**: Suraja Hasarinda ✍️🎨


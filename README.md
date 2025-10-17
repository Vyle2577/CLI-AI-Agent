# 🤖 CLI AI Agent

> A command-line AI agent powered by Google Gemini that can interact with your file system and execute Python code autonomously.

## ✨ Overview

This project provides an intelligent CLI assistant that can navigate directories, read and write files, and execute Python scripts—all through natural language commands. The agent operates within a secure, restricted environment to ensure safe file system operations.

## 🚀 Features

### 📁 File System Operations

- **Get File Info**: Retrieve metadata about files and directories

  - File/directory name
  - File size
  - Directory status (True/False)

- **Get File Contents**: Read and display file contents

  - Returns file content as a string
  - Automatically truncates at 10,000 characters for large files

- **Write File**: Create or modify files
  - Write content to existing files
  - Automatically creates new files if they don't exist

### 🐍 Python Code Execution

- **Run Python File**: Execute Python scripts with AI assistance
  - Open, read, and write to `.py` files
  - Request code reviews and suggestions
  - Get help with debugging and optimization

## 🔒 Security & Restrictions

### 🛡️ Working Directory Constraints

The AI agent is restricted to operate only within a specified working directory. It cannot access or modify files outside this designated area, ensuring your system remains secure.

### ⏱️ Timeout Protection

All operations are subject to a 30-second timeout limit to prevent:

- Infinite recursion
- Runaway processes
- Resource exhaustion

## ⚡ Powered By

This agent uses **Google Gemini** as its AI engine, providing intelligent responses and code analysis capabilities.

## 💻 Usage Instructions

After cloning the repo, use normal CLI commands inside the project directory.

### Syntax

```bash
python3 main.py [--verbose] [Prompt]
```

## 🎯 Use Cases

- Automated file management
- Code review and refactoring
- Batch file operations
- Python script execution and debugging
- Directory exploration and analysis

## ⚠️ Safety First

The built-in restrictions ensure that the AI operates safely within defined boundaries, making it suitable for development workflows without risking system-wide changes.

---

**Note**: Always review AI-generated code and file modifications before deploying to production environments.

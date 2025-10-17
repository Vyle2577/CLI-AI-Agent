import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    """
    run_python_file

    :param path working_directory: working dir boundary for client
    :param path file_path: target file
    :param list args: list of args/commands to send to client, defaults to []
    :return string: STDOUT & STDERROR(if caught) returned in string
    """
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_path = os.path.abspath(working_directory)

    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    command = ["python3", target_file] + args

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            cwd=working_dir_path,
            timeout=30,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        return f"Error: Process exited with code {e.returncode}\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"

    if result.stdout is None or result.stdout == "":
        return "Script executed. No output produced"

    return f"STDOUT: {result.stdout}"

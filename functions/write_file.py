import os

from google.genai import types


def write_file(working_directory, file_path, content):
    """
    :param path working_directory: working directory boundaries
    :param path file_path: target file
    :param string content: content to write to file
    :return string|error: confirmation string returned unless error caught
    """
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_path = os.path.abspath(working_directory)

    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    parent_dir = os.path.dirname(target_file)

    if not parent_dir:
        parent_dir = working_dir_path
    if not os.path.exists(parent_dir):
        try:
            os.makedirs(parent_dir, exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"

    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target_file, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes the given 'content' argument to the specified file path. Creates file if none exists, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to write to, creates file if none exists, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to specified file.",
            ),
        },
    ),
)

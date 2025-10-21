import os

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    """
    :param path working_directory: working directory boundaries
    :param path file_path: target file
    :return string: returns file contents as string
    """
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_path = os.path.abspath(working_directory)

    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:

        with open(target_file, "r") as file:
            content = file.read()
            if len(content) > MAX_CHARS:
                truncated = f'[...File "{file_path}" truncated at 10000 characters]'
                return f"{content[:MAX_CHARS]}\n{truncated}"
            return content

    except FileNotFoundError as e:
        return f"Error: {e}"

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="reads target file and returns file's contents. Truncated at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to retrieve contents from, relative to the working directory.",
            ),
        },
    ),
)

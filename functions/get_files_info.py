import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    """
    :param path working_directory: working dir boundary for client
    :param path directory: directory to search, defaults to "."
    :return string: returns file info (name, size, dir_check)
    """
    target_directory = os.path.abspath(os.path.join(working_directory, directory))
    working_dir_path = os.path.abspath(working_directory)

    if not target_directory.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    directory_contents = os.listdir(target_directory)

    try:

        result_list = []

        for item in directory_contents:
            item_path = os.path.abspath(os.path.join(target_directory, item))
            item_size = os.path.getsize(item_path)
            item_dir_check = os.path.isdir(item_path)
            data_string = (
                f"- {item}: file_size={item_size} bytes, is_dir={item_dir_check}"
            )
            result_list.append(data_string)

        return "\n".join(result_list)

    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

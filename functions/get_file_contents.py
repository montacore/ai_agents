import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_path = os.path.commonpath([abs_path, file_path]) == abs_path
        items = []
        for item in os.listdir(target_dir):
            if os.path.isdir(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            if not valid_target_path:
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            else:
                item_path = os.path.normpath(os.path.join(target_file, item))
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read(MAX_CHARS)
                    if f.read(1):
                        content += f'File "{file_path}" truncated at {MAX_CHARS} characters'
                    
        return "\n".join(items)
    except Exception as e: 
        return f"Error: {e}"

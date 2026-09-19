import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_path = os.path.commonpath([abs_path, target_path]) == abs_path
        if os.path.isdir(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            with open(target_path, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'File "{file_path}" truncated at {MAX_CHARS} characters'
                        
        return content
    except Exception as e: 
        return f"Error: {e}"

schema_get_file_content = {
   "type": "function",
    "function": {
        "name": "get_file_content", 
        "description": "Display the contents of a file with a hard limit of 10000 characters, MAX_CHARS variable set in configs.py",
        "parameters": {
            "type": "object",
            "properties": {
                "required": {
                    "file_path": {
                        "type": "string",
                        "description": "File name from which to display contents, file must be within the working directory"
                },
                },
            },
        },
    },
}

import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        items = []
        for item in os.listdir(target_dir):
            if not os.path.isdir(target_dir):
                return f'Error: "{directory}" is not a directory'
            if not valid_target_dir:
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            else:
                item_dir = os.path.normpath(os.path.join(target_dir, item))
                items.append(f"- {item}: file_size={os.path.getsize(item_dir)} bytes, is_dir={os.path.isdir(item_dir)}")
        return "\n".join(items)
    except Exception as e: 
        return f"Error: {e}"



import os

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try: 
        absolute_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_path]
            command_output = subprocess.run(target_directory, text=True,
                                            capture_output=True, timeout=30)
            if command_output.returncode != 0:
                output = f"Process exited with code {command_output.returncode}"
            if not command_output.stdout and not command_output.stderr:
                output += "No output produced"
            else:
                output += f'STDOUT: {command_output.stdout}'
                output += f'STDERR: {command_output.stderr}'
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'

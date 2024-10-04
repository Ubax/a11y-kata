import os


def print_files_in_directory(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.txt') or "TODO" in file or ".git" in root:
                continue
            # Construct the full file path
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    # Sort filepaths
    file_paths.sort()

    for file in file_paths:
        relative_path = os.path.relpath(file, directory)
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"::::::: Content of {relative_path}:\n{content}\n\n\n")
        except Exception as e:
            print(f"Could not read {file}: {e}\n")


# Specify the directory you want to search
print_files_in_directory(os.getcwd())

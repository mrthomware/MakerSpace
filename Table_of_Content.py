import os

def get_directories(path, parent_path=""):
    """Return a dict where keys are directory names and values are dicts representing subdirectories."""
    directories = {}
    for d in os.listdir(path):
        full_path = os.path.join(path, d)
        if os.path.isdir(full_path):
            if parent_path:
                directories[f"{parent_path}/{d}"] = get_directories(full_path, f"{parent_path}/{d}")
            else:
                directories[d] = get_directories(full_path, d)
    return directories

def add_to_readme_toc(directories, indent=0):
    """Recursively add directories to the table of contents."""
    toc = ""
    for directory, subdirectories in sorted(directories.items()):
        toc += f"{'    ' * indent}- [{directory.split('/')[-1]}]({directory})\n"
        toc += add_to_readme_toc(subdirectories, indent + 1)
    return toc

def update_readme_toc(readme_path, toc):
    """Update the table of contents in the README.md file with the given table of contents."""
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Find the start and end lines of the table of contents
    start_line = None
    end_line = None
    for i, line in enumerate(lines):
        if line.strip() == "## Table of Contents":
            start_line = i
        elif line.strip() == "## About":
            end_line = i
            break

    if start_line is None or end_line is None:
        raise Exception("Could not find the start or end of the table of contents in the README.md file")

    # Remove the existing table of contents
    del lines[start_line+1:end_line]

    # Add the new table of contents
    lines[start_line+1:start_line+1] = [f"{line}\n" for line in toc.split('\n') if line]

    # Write the updated README.md file
    with open(readme_path, 'w') as file:
        file.writelines(lines)

def main():
    # You should replace the below path with the actual path to your 'data' directory
    data_path = data_path = "C:\\Users\\thomw\\Desktop\\data"

    # You should replace the below path with the actual path to your README.md file
    readme_path = r"C:\Users\thomw\Desktop\data\README.md"


    directories = get_directories(data_path)
    toc = add_to_readme_toc(directories)
    update_readme_toc(readme_path, toc)

if __name__ == "__main__":
    main()

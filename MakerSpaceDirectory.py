import os

def create_directory_structure(readme_file, root_dir):
    with open(readme_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('#'):
            # Count the number of '#' to determine the directory level
            level = line.count('#', 0, line.find(' '))
            # Remove '#' and leading/trailing whitespaces, replace spaces with underscores
            dir_name = line.replace('#', '').strip().replace(' ', '_').replace(':', '-')
            
            # Create the directory path based on the level
            dir_path = os.path.join(root_dir, *[''] * (level - 1), dir_name)

            # Create the directory
            os.makedirs(dir_path, exist_ok=True)

# Usage
create_directory_structure('README.md', 'MakerSpace')

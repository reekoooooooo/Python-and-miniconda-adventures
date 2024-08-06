import os

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        new_name = prefix + filename
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

# Usage
rename_files('path/to/your/directory', 'prefix_')







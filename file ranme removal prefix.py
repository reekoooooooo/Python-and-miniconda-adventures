import os

def remove_prefix(directory, prefix):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            new_name = filename[len(prefix):]
            print(f"Renaming '{filename}' to '{new_name}'")  # Debug statement
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        else:
            print(f"Skipping '{filename}' as it does not start with '{prefix}'")  # Debug statement

# Usage
remove_prefix(r'C:\Users\tyrek\OneDrive\Documents', 'prefix_')






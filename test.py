import os

# Get the current directory (where your Python script is located)
current_directory = os.path.dirname(__file__)

# Specify the path to the "cogs" folder using os.path.join()
cogs_folder_path = os.path.join(current_directory, "cogs")

# Call os.listdir() to get the list of filenames in the "cogs" folder
file_list_in_cogs = os.listdir(cogs_folder_path)

# Print the list of filenames in the "cogs" folder
print(file_list_in_cogs)

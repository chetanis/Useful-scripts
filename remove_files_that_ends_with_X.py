# Script Name: remove_files_that_end_with_X.py
# Description: This script removes the files of a specified folder that ends with a specific word.
# Author: [chetanis]

import os

def remove_files_from_folder_that_end_with(input_folder, end_sequence):
    # Ensure the input folder exists
    if not os.path.isdir(input_folder):
        raise FileNotFoundError(f"The folder '{input_folder}' does not exist.")
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(end_sequence):  # Process only files that end with the specified sequence
            file_to_delete = os.path.join(input_folder, filename)
            try:
                os.remove(file_to_delete)  # Attempt to remove the file
                print(f"File '{file_to_delete}' has been removed.")
            except Exception as e:
                print(f"Error removing '{file_to_delete}': {str(e)}")


# Example usage
input_folder = '/input_folder'  # Folder with the files to process

end_sequence = 'copy.pdf'  # The end sequence to match (make sure it's lowercase and includes the file extension)

remove_files_from_folder_that_end_with(input_folder, end_sequence)
# Script Name: remove_last_page_from_pdfs.py
# Description: This script removes the last page from all PDF files in a specified folder.
# Author: [chetanis]
# Dependencies: 
# - PyPDF2: Used to read and manipulate PDF files. It allows you to extract pages, merge PDFs, and perform other operations. Install with `pip install PyPDF2`.
# - PyCryptodome: Required for handling encrypted PDF files. PyPDF2 uses it for advanced encryption algorithms like AES. Install with `pip install PyCryptodome`.


import os
import PyPDF2
from PyPDF2.errors import DependencyError

def remove_last_page_from_folder(input_folder, output_folder):
    # Ensure the output folder exists, or create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):  # Process only PDF files
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with open(input_path, 'rb') as input_file:
                    pdf_reader = PyPDF2.PdfReader(input_file)
                    num_pages = len(pdf_reader.pages)

                    if num_pages > 1:  # Ensure there's more than one page
                        pdf_writer = PyPDF2.PdfWriter()

                        # Add all pages except the last one
                        for i in range(num_pages - 1):
                            pdf_writer.add_page(pdf_reader.pages[i])

                        with open(output_path, 'wb') as output_file:
                            pdf_writer.write(output_file)

                        print(f"Removed the last page from '{filename}', saved to '{output_path}'")
                    else:
                        print(f"'{filename}' only has one page, skipping.")

            except DependencyError:
                print(f"Could not process '{filename}' due to missing dependencies. "
                      f"Ensure PyCryptodome is installed.")

            except PyPDF2.errors.PdfReadError:
                print(f"Error reading '{filename}'. It might be an encrypted or corrupted PDF.")

            except Exception as e:
                print(f"An error occurred while processing '{filename}': {str(e)}")


# Example usage
input_folder = '/input_folder'  # Folder with the original PDFs

output_folder = '/output_folder'  # Folder for the modified PDFs

remove_last_page_from_folder(input_folder, output_folder)

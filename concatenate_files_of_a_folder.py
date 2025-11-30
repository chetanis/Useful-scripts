# Script Name: concatenate_pdfs.py
# Description: This script concatenates all PDF files in a specified folder into a single PDF file.
# Author: [chetanis]
# Dependencies: 
# - PyPDF2: Used to read and manipulate PDF files. It allows you to extract pages, merge PDFs, and perform other operations. Install with `pip install PyPDF2`.
# - PyCryptodome: Required for handling encrypted PDF files. PyPDF2 uses it for advanced encryption algorithms like AES. Install with `pip install PyCryptodome`.

import os
import PyPDF2
from PyPDF2.errors import DependencyError

def concatenate_pdfs_from_folder(input_folder, output_file):
    # Create a PDF writer object to merge the PDFs
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):  # Process only PDF files
            input_path = os.path.join(input_folder, filename)

            try:
                with open(input_path, 'rb') as input_file:
                    pdf_reader = PyPDF2.PdfReader(input_file)

                    # Add all pages from the current PDF to the writer object
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[page_num])

                    print(f"Added pages from '{filename}' to the output file.")

            except DependencyError:
                print(f"Could not process '{filename}' due to missing dependencies. "
                      f"Ensure PyCryptodome is installed.")

            except PyPDF2.errors.PdfReadError:
                print(f"Error reading '{filename}'. It might be an encrypted or corrupted PDF.")

            except Exception as e:
                print(f"An error occurred while processing '{filename}': {str(e)}")

    # Write the concatenated PDF to the output file
    try:
        with open(output_file, 'wb') as output_file_obj:
            pdf_writer.write(output_file_obj)
        print(f"Concatenated PDFs have been saved to '{output_file}'")
    except Exception as e:
        print(f"An error occurred while saving the output file: {str(e)}")


# Example usage
input_folder = '/input_folder'  # Folder with the PDF files to concatenate
output_file = '/output_folder/concatenated_output.pdf'  # The output file name

input_folder = input('Input folder path: ')
output_file = input('Output file path (including file name): ')

concatenate_pdfs_from_folder(input_folder, output_file)

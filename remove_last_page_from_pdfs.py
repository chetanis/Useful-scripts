# Script Name: remove_last_page_from_pdfs.py
# Description: This script removes the last page from all PDF files in a specified folder.
# Author: chetanis
# Dependencies: 
# - PyMuPDF (fitz): Used to read and manipulate PDF files. It allows you to extract pages, merge PDFs, and perform other operations. Install with `pip install PyMuPDF`.

import os
import fitz  # PyMuPDF

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
                pdf_document = fitz.open(input_path)
                num_pages = pdf_document.page_count

                if num_pages > 1:  # Ensure there's more than one page
                    pdf_document.delete_page(num_pages - 1)  # Delete the last page
                    temp_output_path = output_path + ".temp"
                    pdf_document.save(temp_output_path)
                    pdf_document.close()
                    os.replace(temp_output_path, output_path)
                    print(f"Removed the last page from '{filename}', saved to '{output_path}'")
                else:
                    print(f"'{filename}' only has one page, skipping.")

            except Exception as e:
                print(f"An error occurred while processing '{filename}': {str(e)}")

# Example usage
input_folder = '/input_folder'  # Folder with the original PDFs

output_folder = '/output_folder'  # Folder for the modified PDFs

remove_last_page_from_folder(input_folder, output_folder)

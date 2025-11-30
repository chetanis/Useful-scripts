# Script Name: split_pdf_pages.py
# Description: This script splits each page of a PDF into separate PDF files.
# Author: chetanis
# Dependencies: 
# - PyMuPDF (fitz): Used to read and manipulate PDF files. It allows you to extract pages, merge PDFs, and perform other operations. Install with `pip install PyMuPDF`.

import os
import fitz  # PyMuPDF

def split_pdf(input_pdf_path, output_folder):
    """
    Splits each page of a PDF into a separate PDF file.

    :param input_pdf_path: Path to the input PDF file
    :param output_folder: Folder where split pages will be saved
    """
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF
    pdf = fitz.open(input_pdf_path)

    # Loop through each page
    for page_number in range(pdf.page_count):
        # Create a new PDF for the single page
        new_pdf = fitz.open()
        new_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)

        # File name
        output_path = os.path.join(output_folder, f"page_{page_number+1}.pdf")

        # Save the new PDF
        new_pdf.save(output_path)
        new_pdf.close()

        print(f"Saved: {output_path}")

    pdf.close()
    print("\nAll pages successfully split!")


# Example usage
input_pdf = r"inputPdf.pdf"  # Path to the input PDF file
output_dir = r"output_folder"  # Folder where split pages will be saved

split_pdf(input_pdf, output_dir)

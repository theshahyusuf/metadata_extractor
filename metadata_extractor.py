import os
import sys
from PIL import Image
from PyPDF2 import PdfReader  
from docx import Document
import datetime

# Extract metadata from an image file
def extract_image_metadata(file_path):
    with Image.open(file_path) as img:
        metadata = img.info  # Retrieve metadata using PIL's info attribute
    return metadata

# Extract metadata from a PDF file
def extract_pdf_metadata(file_path):
    with open(file_path, 'rb') as f:  # Open file in binary read mode
        pdf = PdfReader(f)  # Read PDF file
        metadata = pdf.metadata  # Extract metadata from PDF
    return metadata

# Extract metadata from a Word document
def extract_docx_metadata(file_path):
    doc = Document(file_path)  # Open DOCX file
    core_properties = doc.core_properties  # Access document properties
    # Extract various metadata fields
    metadata = {
        'author': core_properties.author,
        'title': core_properties.title,
        'subject': core_properties.subject,
        'created': core_properties.created,
        'modified': core_properties.modified,
        'last_modified_by': core_properties.last_modified_by
    }
    return metadata

# Format metadata key for clearer output
def format_metadata_key(key):
    key = key.replace('/', '')  # Remove leading slash for cleaner display
    # Rename specific keys for more clarity
    if key == 'Creator':
        key = 'Software Used to Create File'
    elif key == 'Producer':
        key = 'Conversion Software'
    return key

# Analyze the extracted metadata
def analyze_metadata(metadata):
    analysis = {
        'empty_fields': [],  # Placeholder for fields that are empty
        'timestamp_issues': []  # Placeholder for timestamp related issues
    }

    return analysis

# Generate a report based on extracted and analyzed metadata
def generate_report(metadata, analysis, report_path):
    with open(report_path, 'w') as file:
        file.write("Extracted Metadata:\n")
        # Format and write metadata to the report
        for key, value in metadata.items():
            formatted_key = format_metadata_key(key)
            file.write(f"{formatted_key}: {value}\n")
        file.write("\nMetadata Analysis:\n")
        # Write analysis results to the report
        for key, value in analysis.items():
            formatted_key = format_metadata_key(key)
            file.write(f"{formatted_key}: {value}\n")

# Main function to run the script
def main():
    if len(sys.argv) != 2:
        print("Usage: python metadata_extractor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File does not exist.")
        sys.exit(1)

    # Determine file type and extract metadata
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        metadata = extract_image_metadata(file_path)
    elif file_path.lower().endswith('.pdf'):
        metadata = extract_pdf_metadata(file_path)
    elif file_path.lower().endswith('.docx'):
        metadata = extract_docx_metadata(file_path)
    else:
        print("Unsupported file type.")
        sys.exit(1)

    analysis = analyze_metadata(metadata)
    report_path = 'metadata_report.txt'
    generate_report(metadata, analysis, report_path)
    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()

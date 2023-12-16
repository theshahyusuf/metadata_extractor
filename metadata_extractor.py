import os
import sys
from PIL import Image
from PyPDF2 import PdfReader  
from docx import Document
import datetime

def extract_image_metadata(file_path):
    with Image.open(file_path) as img:
        metadata = img.info
    return metadata

def extract_pdf_metadata(file_path):
    with open(file_path, 'rb') as f:
        pdf = PdfReader(f)  
        metadata = pdf.metadata
    return metadata

def extract_docx_metadata(file_path):
    doc = Document(file_path)
    core_properties = doc.core_properties
    metadata = {
        'author': core_properties.author,
        'title': core_properties.title,
        'subject': core_properties.subject,
        'created': core_properties.created,
        'modified': core_properties.modified,
        'last_modified_by': core_properties.last_modified_by
    }
    return metadata

def format_metadata_key(key):
    key = key.replace('/', '')  # Remove leading slash
    if key == 'Creator':
        key = 'Software Used to Create File'
    elif key == 'Producer':
        key = 'Conversion Software'
    return key

def analyze_metadata(metadata):
    analysis = {'empty_fields': [], 'timestamp_issues': []}
    # ... Add analysis logic here
    return analysis

def generate_report(metadata, analysis, report_path):
    with open(report_path, 'w') as file:
        file.write("Extracted Metadata:\n")
        for key, value in metadata.items():
            formatted_key = format_metadata_key(key)
            file.write(f"{formatted_key}: {value}\n")
        file.write("\nMetadata Analysis:\n")
        for key, value in analysis.items():
            formatted_key = format_metadata_key(key)
            file.write(f"{formatted_key}: {value}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python metadata_extractor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File does not exist.")
        sys.exit(1)

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

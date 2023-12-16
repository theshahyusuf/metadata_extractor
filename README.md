Metadata Extractor Tool
Description
The Metadata Extractor Tool is a Python-based utility designed for cybersecurity and privacy-focused users. Its primary function is to extract metadata from various file types, including images (PNG, JPEG), PDFs, and Word documents (DOCX), without relying on external, public services. This approach ensures user data privacy and security, as the entire operation is conducted locally on the user's system.

First Iteration Notice
Please note that this is the first iteration of the Metadata Extractor Tool. Future updates and enhancements are planned to expand its capabilities and improve its performance.

Installation
Clone the Repository: git clone: https://github.com/theshahyusuf/metadata_extractor
Navigate to the Repository Folder:cd metadata-extractor-tool

Dependencies:
Python 3.x
PIL (Pillow)
PyPDF2
python-docx
Install these dependencies using pip: pip install Pillow PyPDF2 python-docx

Usage
Run the tool from the command line by passing the file path as an argument: python metadata_extractor.py <path_to_file>

The tool will generate a report metadata_report.txt in the same directory, containing the extracted metadata and any analysis results.

Contributing
Contributions to the Metadata Extractor Tool are welcome. Please ensure to follow best practices for code contributions and adhere to the existing coding style.



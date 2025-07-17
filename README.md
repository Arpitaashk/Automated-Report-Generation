Automated Report Generator

This project automates the generation of Excel and PDF reports using Python. It takes user inputs or existing data and produces well-formatted output reports. Designed for ease of use, this CLI-based tool is ideal for anyone looking to streamline repetitive report generation tasks.



 Features

-  Accepts user input or loads data from files
-  Generates customized Excel reports with formatting
-  Creates PDF reports with structured layouts
-  Customizable fonts, styles, and sections
-  Automatically saves outputs to specified directory

 Project Structure

Automated-Report-Generation/
├── report_generator.py # Main script
├── templates/ # Optional folder for layout or assets
├── output/ # Generated Excel/PDF files
└── README.md


Tech Stack

- **Python 3**
- [`openpyxl`](https://openpyxl.readthedocs.io/) – for Excel file generation and formatting
- [`reportlab`](https://www.reportlab.com/dev/docs/) – for PDF creation
- `os`, `datetime`, `argparse` – for file management and CLI support

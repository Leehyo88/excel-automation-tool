# Excel Automation Tool

A simple Python tool to merge multiple Excel files into one spreadsheet and remove duplicate rows.

## Features

- Merge multiple `.xlsx` files from a folder.
- Remove duplicate rows.
- Export the result to a new Excel file.
- Keep the original source files unchanged.

## Requirements

- Python 3
- pandas
- openpyxl

## Installation

Install the required libraries:

```bash
py -m pip install pandas openpyxl
```

## How to Use

1. Place your `.xlsx` files in one folder.
2. Run the program:

   ```bash
   py gop_excel.py
   ```

3. Enter the folder path when prompted.
4. Find `Ket_qua_gop.xlsx` in the same folder.

## Disclaimer

Test with sample files before using important data. Input files should have compatible column structures.

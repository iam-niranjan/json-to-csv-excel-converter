# JSON to CSV/Excel Converter

This repository contains a simple Python script to convert JSON files to CSV or Excel format. The script allows you to convert individual JSON files or combine multiple JSON files into a single Excel file.

## Features

- Convert JSON files to CSV format.
- Convert JSON files to Excel format.
- Combine multiple JSON files into a single Excel file.
- User-friendly command-line interface to select input files and output formats.

## Requirements

- Python 3.x
- pandas library (for Excel conversion)
- openpyxl library (for Excel conversion)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/json-to-csv-excel-converter.git
    cd json-to-csv-excel-converter
    ```

2. Install the required dependencies:

    ```sh
    pip install pandas openpyxl
    ```
# JSON to CSV/Excel Converter

This repository contains a simple Python script to convert JSON files to CSV or Excel format. The script allows you to convert individual JSON files or combine multiple JSON files into a single Excel file.

## Features

- Convert JSON files to CSV format.
- Convert JSON files to Excel format.
- Combine multiple JSON files into a single Excel file.
- User-friendly command-line interface to select input files and output formats.

## Requirements

- Python 3.x
- pandas library (for Excel conversion)
- openpyxl library (for Excel conversion)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/json-to-csv-excel-converter.git
    cd json-to-csv-excel-converter
    ```

2. Install the required dependencies:

    ```sh
    pip install pandas openpyxl
    ```

Running the script and selecting data.json with the output format as CSV will generate output/data.csv with the following content:

```csv
name,age
Alice,30
Bob,25
```

Selecting the output format as Excel will generate output/data.xlsx with the same data.

### Combining Multiple JSON Files

If you choose to convert all files, the script will combine the data from all JSON files in the `input` folder and generate a single Excel file `output/combined.xlsx`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.



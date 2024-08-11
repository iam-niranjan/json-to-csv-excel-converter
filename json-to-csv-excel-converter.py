import os
import json
import csv
import pandas as pd
from pathlib import Path

def json_to_csv(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

def json_to_excel(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def combine_json_to_excel(input_files, output_file):
    combined_data = []
    for input_file in input_files:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                combined_data.extend(data)
            else:
                combined_data.append(data)

    if combined_data:
        df = pd.DataFrame(combined_data)
        df.to_excel(output_file, index=False)
    else:
        print("No data to combine.")

def main():
    input_folder = Path('input')
    output_folder = Path('output')
    output_folder.mkdir(exist_ok=True)

    json_files = list(input_folder.glob('*.json'))

    if not json_files:
        print("No JSON files found in the input folder.")
        return

    print("Available JSON files:")
    for i, file in enumerate(json_files, 1):
        print(f"{i}. {file.name}")

    print("0. Convert all files")

    choice = input("Enter the number of the file you want to convert or '0' to convert all files: ").strip()

    if choice == '0':
        output_format = input("Enter the output format (csv/xlsx): ").lower()
        if output_format == 'xlsx':
            output_file = output_folder / 'combined.xlsx'
            combine_json_to_excel(json_files, output_file)
            print(f"Conversion complete. Output file: {output_file}")
        else:
            print("Combining multiple files into a single CSV is not supported. Please choose 'xlsx'.")
            return
    else:
        try:
            file_choice = int(choice) - 1
            input_file = json_files[file_choice]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number or '0'.")
            return

        output_format = input("Enter the output format (csv/xlsx): ").lower()

        output_file = output_folder / f"{input_file.stem}.{output_format}"

        if output_format == 'csv':
            json_to_csv(input_file, output_file)
        elif output_format == 'xlsx':
            json_to_excel(input_file, output_file)
        else:
            print("Invalid output format. Please choose 'csv' or 'xlsx'.")
            return

        print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    main()

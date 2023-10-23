import os
import re
import csv
from pathlib import Path

def process_log_file(log_path):
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()

        pattern = (
            r'Epoch : (\d+)\s+Train Loss\s+:\s+([\d.]+)\s+\|\s+Train Accuracy\s+:\s+([\d.]+)\s+' 
            r'\nVal Loss\s+:\s+([\d.]+)\s+\|\s+Val Accuracy\s+:\s+([\d.]+)'
        )

        matches = re.findall(pattern, log_content)

        if matches:
            csv_data = [
                ['Epoch', 'Train Loss', 'Train Accuracy', 'Val Loss', 'Val Accuracy']
            ]

            for match in matches:
                csv_data.append(list(match))

            return csv_data
        else:
            return None

def convert_logs_to_csv(logs_folder, output_folder):
    logs_path = Path(logs_folder)
    output_path = Path(output_folder)

    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Process each log file in the logs folder
    for log_file in logs_path.glob('*.log'):
        csv_data = process_log_file(log_file)

        if csv_data:
            csv_filename = f'{log_file.stem}.csv'
            csv_path = output_path / csv_filename

            # Write CSV file
            with open(csv_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(csv_data)

            print(f'Converted {log_file} to {csv_path}')

if __name__ == '__main__':
    logs_folder = 'log'
    output_folder = 'plots_csv'

    convert_logs_to_csv(logs_folder, output_folder)

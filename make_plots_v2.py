import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to plot CSV
def plot_csv_split(csv_path, output_folder):
    df = pd.read_csv(csv_path)
    run_number = os.path.splitext(os.path.basename(csv_path))[0]

    # Check if the dataframe has more than 30 rows
    if len(df) > 30:
        # Split the dataframe into two halves
        df1 = df.iloc[:len(df)//2]
        df2 = df.iloc[len(df)//2:]

        # Plot for the first half
        plot_df(df1, run_number, output_folder, suffix='_part1')

        # Plot for the second half
        plot_df(df2, run_number, output_folder, suffix='_part2')
    else:
        # If less than or equal to 30 rows, plot the whole dataframe
        plot_df(df, run_number, output_folder)

# Function to plot a dataframe
def plot_df(df, run_number, output_folder, suffix=''):
    plt.figure(figsize=(12, 6))

    # Plot Train Accuracy and Val Accuracy
    plt.plot(df['Epoch'], df['Train Accuracy'], label='Train Accuracy')
    plt.plot(df['Epoch'], df['Val Accuracy'], label='Validation Accuracy')
    plt.title(f'Run {run_number} - Accuracy{suffix}')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'plot_{run_number}_accuracy{suffix}.png'))
    plt.close()

# Output folder
output_folder = 'plots'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each CSV file in 'plots_csv' folder
csv_folder = 'plots_csv'
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        csv_path = os.path.join(csv_folder, csv_file)
        plot_csv_split(csv_path, output_folder)

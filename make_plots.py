import os
import pandas as pd
import matplotlib.pyplot as plt

# Create 'plots' folder if it doesn't exist
plots_folder = 'plots'
if not os.path.exists(plots_folder):
    os.makedirs(plots_folder)

# Get all CSV files in 'plots_csv' folder
csv_folder = 'plots_csv'
csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

# Iterate through each CSV file
for csv_file in csv_files:
    # Read CSV file into a DataFrame
    csv_path = os.path.join(csv_folder, csv_file)
    df = pd.read_csv(csv_path)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Epoch'], df['Train Accuracy'], label='Train Accuracy')
    plt.plot(df['Epoch'], df['Val Accuracy'], label='Validation Accuracy')
    plt.title(f'Training Progress - {csv_file[:-4]}')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    # Save the plot in the 'plots' folder
    plot_name = f"{csv_file[:-4]}_plot.png"
    plot_path = os.path.join(plots_folder, plot_name)
    plt.savefig(plot_path)
    plt.close()

print("Plots generated successfully!")

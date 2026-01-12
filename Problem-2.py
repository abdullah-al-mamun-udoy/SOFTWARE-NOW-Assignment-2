import os
import pandas as pd
import numpy as np


# Full path of my temperatures folder.
FOLDER_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)/temperatures"

# List all CSV files in the folder
csv_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith(".csv")]

all_data = []

for file in csv_files:
    file_path = os.path.join(FOLDER_PATH, file)

    # Read one CSV file into a pandas DataFrame
    data_frame = pd.read_csv(file_path)

    # Store the DataFrame in a list
    all_data.append(data_frame)

# Combine all DataFrames into one DataFrame
combined_data = pd.concat(all_data, ignore_index=True)



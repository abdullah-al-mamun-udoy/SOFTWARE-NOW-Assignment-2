import os
import pandas as pd
import numpy as np


# Full path of my temperatures folder.
# path of my output folder
FOLDER_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)/temperatures"
OUTPUT_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)"

# List all CSV files in the folder
csv_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith(".csv")]

#all_dataframes = []
all_data = []

for file in csv_files:
    file_path = os.path.join(FOLDER_PATH, file)
    
    # Read each CSV file
    df = pd.read_csv(file_path)
    all_data.append(df)

# Combine all CSVs
combined_data = pd.concat(all_data, ignore_index=True)


# Month columns in CSV
month_columns = ["January","February","March","April","May","June","July","August",
                 "September","October","November","December"]

# Melt the DataFrame: one row per station per month
long_data = pd.melt(
    combined_data,
    id_vars=["STATION_NAME", "STN_ID", "LAT", "LON"],
    value_vars=month_columns,
    var_name="Month",
    value_name="Temperature"
)


# Convert month names to numbers
month_to_num = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

long_data["Month_Num"] = long_data["Month"].map(month_to_num)


# Assign Australian seasons
def get_season(month):
    if month in [12,1,2]:
        return "Summer"
    elif month in [3,4,5]:
        return "Autumn"
    elif month in [6,7,8]:
        return "Winter"
    else:
        return "Spring"

long_data["Season"] = long_data["Month_Num"].apply(get_season)


# Convert Temperature to numeric
long_data["Temperature"] = pd.to_numeric(long_data["Temperature"], errors="coerce")


# Seasonal average temperature
def seasonal_average(data):
    result = data.groupby("Season")["Temperature"].mean()
    file = open(OUTPUT_PATH + "/average_temp.txt", "w")
    for season in result.index:
        file.write(f"{season}: {result[season]:.1f}°C\n")
    file.close()

# Station temperature range
def largest_range(data):
    stats = data.groupby("STATION_NAME")["Temperature"].agg(["max", "min"])
    stats["range"] = stats["max"] - stats["min"]

    max_range = stats["range"].max()
    stations = stats[stats["range"] == max_range]

    file = open(OUTPUT_PATH + "/largest_temp_range_station.txt", "w")
    for station, row in stations.iterrows():
        file.write(
            f"Station {station}: Range {row['range']:.1f}°C "
            f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
        )
    file.close()

# Temperature stability (standard deviation)
def temperature_stability(data):
    std_values = data.groupby("STATION_NAME")["Temperature"].std()

    min_std = std_values.min()
    max_std = std_values.max()

    stable = std_values[std_values == min_std]
    variable = std_values[std_values == max_std]

    file = open(OUTPUT_PATH + "/temperature_stability_stations.txt", "w")
    for s, v in stable.items():
        file.write(f"Most Stable: Station {s}: StdDev {v:.1f}°C\n")
    for s, v in variable.items():
        file.write(f"Most Variable: Station {s}: StdDev {v:.1f}°C\n")
    file.close()

seasonal_average(data_long)
largest_range(data_long)
temperature_stability(data_long)

# Problem is solved
# Thanks for this interactive problem

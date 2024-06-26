# -*- coding: utf-8 -*-
"""DataPreprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NjXTrNZFIaJab2-JKT_m8db3261yUsyW
"""

import pandas as pd

# Load the data from Excel
file_path = '/content/StripedG2.xlsx'  # Update this with the path to your Excel file
data = pd.read_excel(file_path)

# Make sure to convert the 'Total Damage, Adjusted' column to numeric, handling non-numeric gracefully
data['Total Damage, Adjusted (\'000 US$)'] = pd.to_numeric(data['Total Damage, Adjusted (\'000 US$)'], errors='coerce')

# Calculate average damages where damages are not zero
average_damages = data[data['Total Damage, Adjusted (\'000 US$)'] > 0].groupby('Disaster Subgroup')['Total Damage, Adjusted (\'000 US$)'].mean()

# Function to replace zero damages with the subgroup average
def replace_zero_damages(row):
    if row['Total Damage, Adjusted (\'000 US$)'] == 0:
        return average_damages.get(row['Disaster Subgroup'], 0)  # Default to 0 if no average is available
    else:
        return row['Total Damage, Adjusted (\'000 US$)']

# Replace zeros with the computed averages
data['Total Damage, Adjusted (\'000 US$)'] = data.apply(replace_zero_damages, axis=1)

# Save the updated DataFrame to a new Excel file
output_path = 'outG2.xlsx'  # Update this with the path where you want to save the updated file
data.to_excel(output_path, index=False)

print("Data processing complete and saved to:", output_path)

file_path = '/content/outG2.xlsx'  # Update this with the path to your Excel file
df = pd.read_excel(file_path)

df['Disaster Subtype'] = df['Disaster Subtype'].astype(str)
df['Disaster Group'] = df['Disaster Group'].astype(str)
df['Disaster Subgroup'] = df['Disaster Subgroup'].astype(str)
df['Location'] = df['Location'].astype(str)

output_path = 'outG2V2.xlsx'  # Update this with the path where you want to save the updated file
data.to_excel(output_path, index=False)
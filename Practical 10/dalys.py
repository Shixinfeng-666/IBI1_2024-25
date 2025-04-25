import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/Users/wsr/Desktop/IBI1_2024-25/Practical 10')

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Verify working directory
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())


# Working with dataframes
# Display first 5 rows (and the title)
print("\nFirst 5 rows:")
print(dalys_data.head(5))

# Show dataframe information
print("\nDataframe info:")
print(dalys_data.info())

# Basic statistics
print("\nDescriptive statistics:")
print(dalys_data.describe())

# Access specific values
print("\nThird column (Year) for first 10 rows:")
print(dalys_data.iloc[0:10, 2])  # Column indices: 0=Entity, 1=Code, 2=Year, 3=DALYs
# The 10th year in Afghanistan is 1999 (rows are ordered chronologically)

# Boolean indexing for 1990 data
print("\nDALYs in 1990:")
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print(dalys_1990)

# Comparing UK and France
# Extract UK and France data
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]

# Compare mean DALYs
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()
print(f"\nMean DALYs:\nUK: {uk_mean:.1f}\nFrance: {france_mean:.1f}")
# The UK's mean DALYs is smaller than France's (UK: ~23k vs France: ~25k)

# Plot UK DALYs over time
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year, rotation = -90)
plt.show()
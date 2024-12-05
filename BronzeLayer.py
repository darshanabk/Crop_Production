import os
import pandas as pd

# Download the dataset using Kaggle API
os.system("kaggle datasets download -d akshatgupta7/crop-yield-in-indian-states-dataset -p . --unzip")

# Load the dataset
data = pd.read_csv("crop_yield.csv")

# Explore the data
print(data.head())

# Save the preprocessed data
data.to_csv("BronzeLayer_data.csv", index=False)


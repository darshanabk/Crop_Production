import pandas as pd

# Load the dataset
data = pd.read_csv('/kaggle/input/crop-yield-in-indian-states-dataset/crop_yield.csv')

# Explore the data
print(data.head())

# Save the preprocessed data
data.to_csv('BronzeLayer_data.csv', index=False)


# **Indian Crop Yield Dataset**

This repository contains the **Bronze Layer**, which houses the **raw dataset** downloaded from Kaggle: [Crop Yield in Indian States Dataset](https://www.kaggle.com/datasets/akshatgupta7/crop-yield-in-indian-states-dataset/data). 

The Bronze Layer serves as the **source of truth**, preserving the dataset exactly as it was originally obtained, without any modifications or preprocessing. It acts as the foundational layer in the data pipeline, ensuring data integrity and traceability.

## **About the Dataset**

This dataset provides agricultural data for various crops cultivated across Indian states from **1997 to 2020**, encompassing critical factors essential for **crop yield prediction** and agricultural analysis.

### **Columns Description**
- **Crop**: The name of the crop cultivated.
- **Crop_Year**: The year in which the crop was grown.
- **Season**: The specific cropping season (e.g., Kharif, Rabi, Whole Year).
- **State**: The Indian state where the crop was cultivated.
- **Area**: The total land area (in hectares) under cultivation for the specific crop.
- **Production**: The quantity of crop production (in metric tons).
- **Annual_Rainfall**: The annual rainfall received in the crop-growing region (in mm).
- **Fertilizer**: The total amount of fertilizer used for the crop (in kilograms).
- **Pesticide**: The total amount of pesticide used for the crop (in kilograms).
- **Yield**: The calculated crop yield (production per unit area).

## **Purpose of the Bronze Layer**
The **Bronze Layer** is intended to:
1. Preserve the original dataset for **auditability** and reference.
2. Act as the initial stage in the data pipeline, enabling preprocessing and transformation in subsequent layers.
3. Maintain a clear distinction between raw and processed data.

## **Credits**
The dataset is sourced from Kaggle: [Crop Yield in Indian States Dataset](https://www.kaggle.com/datasets/akshatgupta7/crop-yield-in-indian-states-dataset/data).

## **Note**
No changes have been made to the dataset in this layer. For cleaned and processed data, refer to the **Silver Layer** (coming soon).

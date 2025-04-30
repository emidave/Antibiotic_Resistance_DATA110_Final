import pandas as pd
import numpy as np

# Adding the additional variable 'prop_antibiotics_sold_without_prescription' to the merged dataframe
# This is a special variable because we only have it based on the region level, not the country level

# Load the datasets
antibiotics_sold_without_prescription = pd.read_csv("antibiotics_sold_without_prescription.csv")
merged_df = pd.read_csv("data/merged.csv")

def add_antibiotics_column(merged_df, antibiotics_sold_without_prescription):
    # Ensure the 'Region' column is present in both dataframes
    if 'Region' not in merged_df.columns or 'Region' not in antibiotics_sold_without_prescription.columns:
        raise ValueError("Both dataframes must have a 'Region' column.")

    # Merge the dataframes on the 'Region' column
    merged_df = merged_df.merge(
        antibiotics_sold_without_prescription[['Region', 'prop_antibiotics_sold_without_prescription']],
        on='Region',
        how='left'
    )

    # Rename the new column for clarity
    merged_df.rename(columns={'prop_antibiotics_sold_without_prescription': 'Prop_Antibiotics_Sold_Without_Prescription'}, inplace=True)

    return merged_df

# Example usage
merged_df = add_antibiotics_column(merged_df, antibiotics_sold_without_prescription)

# Save the updated merged_df to a new CSV file
merged_df.to_csv('merged_with_antibiotics.csv', index=False)
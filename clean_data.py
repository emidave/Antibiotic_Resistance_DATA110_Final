# This scripts cleans the antibiotic resistance dataset.
# It loads the dataset, replaces 'Empty' values with NaN, converts specified columns to numeric types

import pandas as pd
import numpy as np

def clean_dataset(filepath):
    """
    Loads and cleans the antibiotic resistance dataset.
    
    Args:
        filepath (str): path to CSV file
    Returns:
        pd.DataFrame: cleaned dataframe
    """
    df = pd.read_csv(filepath)
    
    # Replace 'Empty' with NaN
    df = df.replace('Empty', np.nan)

    # List numeric columns
    numeric_cols = ['antimicrobial_mg_per_population', 
                    'kilograms_eggs_per_year_per_capita',
                    'expected_schooling_years', 
                    'ibs_rate_2017',
                    'kilograms_meat_per_year_per_capita',
                    'kilograms_milk_per_year_per_capita',
                    'PercentResistant',
                    'Prop_Antibiotics_Sold_Without_Prescription']

    # Convert numeric columns
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows where target is missing
    df = df.dropna(subset=['PercentResistant'])

    # Reset index
    df = df.reset_index(drop=True)

    return df

# This script recodes the features Milk Consumption, Meat Consumption, and Egg Consumption
# into a single feature called Animal Product Consumption.
#  This variable is for generating our 2nd proportional symbol map in Tableau. 

import pandas as pd

# Importing our dataset
df = pd.read_csv('data/raw/merged_with_antibiotics.csv')

# Recode the features Milk Consumption, Meat Consumption, and Egg Consumption
df['Animal Product Consumption'] = df[['kilograms_milk_per_year_per_capita', 
                                        'kilograms_meat_per_year_per_capita', 
                                        'kilograms_eggs_per_year_per_capita']].sum(axis=1)

# Save the recoded dataset
df.to_csv('data/processed/merged_with_animal_product_consumption.csv', index=False)


# Load the necessary datasets
commodities_data = pd.read_csv('/mnt/data/all_commodities.csv')
obesity_data = pd.read_csv('/mnt/data/Nutrition_Physical_Activity_and_Obesity_Data.csv')

# Display the first few rows of each dataset
commodities_data.head(), obesity_data.head()

# Filter the commodities data for sugar prices
sugar_prices = commodities_data[commodities_data['Commodity'] == 'Sugar']

# Display the first few rows of the filtered sugar prices data
sugar_prices.head()

# Extract the year from the Date-Time column in sugar prices data
sugar_prices['Year'] = pd.to_datetime(sugar_prices['Date-Time']).dt.year

# Calculate the average sugar price for each year
average_sugar_price_per_year = sugar_prices.groupby('Year')['Value'].mean().reset_index()

# Display the first few rows of the average sugar price per year
average_sugar_price_per_year.head()

# Prepare the obesity data for merging by extracting relevant columns
obesity_data_filtered = obesity_data[['YearStart', 'YearEnd', 'LocationAbbr', 'LocationDesc', 'Topic', 'Data_Value']]

# Merge the average sugar price per year with the obesity data based on the YearStart column
merged_data = pd.merge(obesity_data_filtered, average_sugar_price_per_year, left_on='YearStart', right_on='Year', how='inner')

# Display the first few rows of the merged dataset
import ace_tools as tools; tools.display_dataframe_to_user(name="Merged Sugar Prices and Obesity Data", dataframe=merged_data)

merged_data.head()

# Ensure the merged dataset includes data for all regions
obesity_data_filtered_all = obesity_data[['YearStart', 'YearEnd', 'LocationAbbr', 'LocationDesc', 'Topic', 'Data_Value']]

# Merge the average sugar price per year with the obesity data based on the YearStart column
merged_data_all = pd.merge(obesity_data_filtered_all, average_sugar_price_per_year, left_on='YearStart', right_on='Year', how='inner')

# Display the first few rows of the merged dataset
import ace_tools as tools; tools.display_dataframe_to_user(name="Merged Sugar Prices and Obesity Data for All Regions", dataframe=merged_data_all)

merged_data_all.head()


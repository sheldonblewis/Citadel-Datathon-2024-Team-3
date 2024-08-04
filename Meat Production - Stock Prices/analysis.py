# Check the date ranges of both datasets
meat_date_range = (meat_stats_meat_production_data_clean['Date'].min(), meat_stats_meat_production_data_clean['Date'].max())
stock_date_range = (restaurant_stock_data_monthly['Date-Time'].min(), restaurant_stock_data_monthly['Date-Time'].max())

# Ensure that both datasets are using the same date format and granularity
meat_stats_meat_production_data_clean['Date'] = meat_stats_meat_production_data_clean['Date'].dt.to_period('M')
restaurant_stock_data_monthly['Date-Time'] = restaurant_stock_data_monthly['Date-Time'].dt.to_period('M')

# Step 1: Convert date columns to monthly periods
meat_stats_meat_production_data_clean['Date'] = meat_stats_meat_production_data_clean['Date'].dt.to_period('M')
restaurant_stock_data_monthly['Date-Time'] = restaurant_stock_data_monthly['Date-Time'].dt.to_period('M')

# Step 2: Merge the datasets on the monthly period columns
merged_data_corrected = pd.merge(meat_stats_meat_production_data_clean, restaurant_stock_data_monthly, left_on='Date', right_on='Date-Time', how='inner')

# Display summary of the corrected merged data
merged_corrected_info = merged_data_corrected.info()
merged_corrected_head = merged_data_corrected.head()

# Correlation analysis
correlation_matrix = merged_data_corrected[['Production', 'Close']].corr()
correlation_matrix

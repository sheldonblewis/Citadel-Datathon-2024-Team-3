# Correlation analysis
correlation_matrix = merged_data_corrected[['Production', 'Close']].corr()
correlation_matrix

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Prepare the data for regression analysis
X = merged_data_corrected[['Production']]
y = merged_data_corrected['Close']

# Build the regression model
regression_model = LinearRegression().fit(X, y)
regression_summary = {
    'Intercept': regression_model.intercept_,
    'Coefficient': regression_model.coef_[0],
    'R^2': regression_model.score(X, y)
}

# Plotting the regression results
sns.regplot(x='Production', y='Close', data=merged_data_corrected)
plt.title('Regression Analysis of Meat Production vs. Stock Prices')
plt.xlabel('Meat Production (Million Pounds)')
plt.ylabel('Stock Close Price')
plt.show()

regression_summary

# Correlation analysis
correlation_matrix = merged_data_corrected[['Production', 'Close']].corr()
correlation_matrix

# Prepare the data for regression analysis
X = merged_data_corrected[['Production']]
y = merged_data_corrected['Close']

# Build the regression model
regression_model = LinearRegression().fit(X, y)
regression_summary = {
    'Intercept': regression_model.intercept_,
    'Coefficient': regression_model.coef_[0],
    'R^2': regression_model.score(X, y)
}

# Plotting the regression results
sns.regplot(x='Production', y='Close', data=merged_data_corrected)
plt.title('Regression Analysis of Meat Production vs. Stock Prices')
plt.xlabel('Meat Production (Million Pounds)')
plt.ylabel('Stock Close Price')
plt.show()

regression_summary

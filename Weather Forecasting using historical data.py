#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Load historical weather data
data = {'day':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'temperature':[30, 32, 31, 29, 28, 27, 26, 25, 24, 23],
        'humidity':[70, 65, 68, 72, 75, 78, 80, 82, 85, 88],
        'wind_speed':[5, 7, 6, 4, 3, 2, 4, 5, 6, 7],
        'rainfall':[0, 0.1, 0.05, 0, 0.2, 0.3, 0.1, 0, 0.15, 0.25],
        'next_day_temperature':[32, 31, 29, 28, 27, 26, 25, 24, 23, 22],
        'Precipitation':[0, 0.05, 0, 0.2, 0.3, 0.1, 0, 0.15, 0.25, 0.3]}

#convert data into dataframe
weather_df = pd.DataFrame(data)

# Display the dataset
print("Historical Weather Dataset:")
print(weather_df)

# Define features and target variable
X = weather_df[['temperature', 'humidity', 'wind_speed', 'rainfall']]
y_temp = weather_df['next_day_temperature']
y_rain = weather_df['Precipitation']

# Split the dataset into training and testing sets for temperature prediction
X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(X, y_temp, test_size=0.2, random_state=42)

# Create a Linear Regression model for temperature prediction

model_temp = LinearRegression()

# Train the model for temperature prediction
model_temp.fit(X_train_temp, y_train_temp)

# Make predictions on the test set for temperature prediction
y_pred_temp = model_temp.predict(X_test_temp)

# Evaluate the model for temperature prediction
mse_temp = mean_squared_error(y_test_temp, y_pred_temp)
r2_temp = r2_score(y_test_temp, y_pred_temp)

print(f"\nTemperature Prediction - Mean Squared Error: {mse_temp:.2f}")
print(f"Temperature Prediction - R^2 Score: {r2_temp:.2f}")
print("\nTemperature Model Coefficients:")
for feature, coef in zip(X.columns, model_temp.coef_):
    print(f"{feature}: {coef:.4f}")

# plot actual vs predicted temperatures
plt.figure(figsize=(10,6))
plt.plot(y_test_temp.values, label='Actual Temperature', marker='o')
plt.plot(y_pred_temp, label='Predicted Temperature', marker='x')
plt.title('Actual vs Predicted Next Day Temperature')
plt.xlabel('Test Sample Index')
plt.ylabel('Temperature')
plt.legend()
plt.show()

#predict temperature with custom input
custom_input_temp = np.array([[28, 75, 3, 0.2]])
predicted_temp = model_temp.predict(custom_input_temp)
print(f"\nPredicted Next Day Temperature for custom input: {predicted_temp[0]:.2f}°C")

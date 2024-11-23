from google.colab import files
uploaded = files.upload()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel('user_behavior_dataset.csv')

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Get summary statistics
print(data.describe())

print("\nAverage Battery Drain by Device Model:")
print(data.groupby('Device Model')['Battery Drain (mAh/day)'].mean())

# Univariate analysis (distribution of a numerical column)
plt.figure(figsize=(10,6))
sns.histplot(data['Age'], kde=True)
plt.show()

# Bivariate analysis (relationship between two variables)
plt.figure(figsize=(10,6))
sns.scatterplot(x='Age', y='Number of Apps Installed', data=data)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Number of Apps Installed', data=data)
plt.title('Distribution of Apps Installed by Gender')
plt.show()

# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='App Usage Time (min/day)', hue='Gender', data=data)
plt.title("Age vs App Usage Time")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Data Usage (MB/day)', hue='Gender', data=data)
plt.title("Age vs Data Usage")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Device Model'], bins=20, kde=True)
plt.title("Distribution of Device Models")
plt.show()

# Clustering
features = data[['App Usage Time (min/day)', 'Battery Drain (mAh/day)', 'Screen On Time (hours/day)', 'Data Usage (MB/day)']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=0)
data['Cluster'] = kmeans.fit_predict(features_scaled)
sns.pairplot(data, hue='Cluster', vars=['App Usage Time (min/day)', 'Battery Drain (mAh/day)', 'Screen On Time (hours/day)', 'Data Usage (MB/day)'])
plt.show()

# Histograms and Box Plots
plt.figure(figsize=(10, 6))
sns.histplot(data['App Usage Time (min/day)'], bins=20, kde=True)
plt.title("Distribution of App Usage Time")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='User Behavior Class', y='App Usage Time (min/day)', data=data)
plt.title("Box Plot of App Usage Time by User Behavior Class")
plt.show()

# Predicting User Behavior Class (Logistic Regression)
X = data[['App Usage Time (min/day)', 'Battery Drain (mAh/day)', 'Screen On Time (hours/day)', 'Data Usage (MB/day)']]
y = data['User Behavior Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Scaling the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training logistic regression model
model = LogisticRegression(max_iter=500)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n")

# Battery Drain Prediction (Linear Regression)
X_battery = data[['App Usage Time (min/day)', 'Screen On Time (hours/day)', 'Data Usage (MB/day)']]
y_battery = data['Battery Drain (mAh/day)']

# Training linear regression model
battery_model = LinearRegression()
battery_model.fit(X_battery, y_battery)
data['Battery Prediction'] = battery_model.predict(X_battery)

mae = mean_absolute_error(data['Battery Drain (mAh/day)'], data['Battery Prediction'])
mse = mean_squared_error(data['Battery Drain (mAh/day)'], data['Battery Prediction'])
rmse = np.sqrt(mse)
r2 = r2_score(data['Battery Drain (mAh/day)'], data['Battery Prediction'])

print("Regression Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")

# Plotting Actual vs Predicted Battery Drain
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Battery Drain (mAh/day)', y='Battery Prediction', data=data)
plt.title("Actual vs Predicted Battery Drain")
plt.show()

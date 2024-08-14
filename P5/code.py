import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dataset.csv')

# Display the original data
print("Original Data:")
print(df)

# Step 3: Data Transformation
# Normalization
scaler = MinMaxScaler()
df[['Age_Normalized', 'Income_Normalized']] = scaler.fit_transform(df[['Age', 'Income']])

# Standardization
scaler = StandardScaler()
df[['Age_Standardized', 'Income_Standardized']] = scaler.fit_transform(df[['Age', 'Income']])

print("\nData after Normalization and Standardization:")
print(df)

# Step 4: Data Discretization
df['Age_Bins'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70], labels=['20-30', '30-40', '40-50', '50-60', '60-70'])
df['Income_Bins'] = pd.cut(df['Income'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])

print("\nData after Discretization:")
print(df)

# Step 5: Summary and Visualization
print("\nSummary of Transformed Data:")
print(df.describe())

# Visualization
plt.figure(figsize=(12, 6))

# Age distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], bins=5, kde=True)
plt.title('Age Distribution')

# Income distribution
plt.subplot(1, 2, 2)
sns.histplot(df['Income'], bins=4, kde=True)
plt.title('Income Distribution')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

# Age Bins
plt.subplot(1, 2, 1)
sns.countplot(x='Age_Bins', data=df)
plt.title('Age Bins')

# Income Bins
plt.subplot(1, 2, 2)
sns.countplot(x='Income_Bins', data=df)
plt.title('Income Bins')

plt.tight_layout()
plt.show()

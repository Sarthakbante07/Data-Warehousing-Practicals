from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pandas as pd

# Load datasets
df = pd.read_csv('dataset1.csv')

# Select relevant features
features = df[['age', 'income']]

# Handle missing values by imputing with the mean of each column
imputer = SimpleImputer(strategy='mean')
features_imputed = imputer.fit_transform(features)

# Perform PCA for dimensionality reduction
pca = PCA(n_components=1)
reduced_data = pca.fit_transform(features_imputed)

# Create a DataFrame with the reduced data
df_reduced = pd.DataFrame(reduced_data, columns=['principal_component'])
df_reduced['id'] = df['id']
df_reduced['gender'] = df['gender']

# Display reduced data
print("\nReduced Data:")
print(df_reduced)

# Plot the reduced data
plt.figure(figsize=(8, 6))
plt.scatter(df_reduced['principal_component'], df_reduced['gender'].apply(lambda x: 1 if x == 'Male' else 0), c='blue')
plt.title('Reduced Data')
plt.xlabel('Principal Component')
plt.ylabel('Gender (0=Female, 1=Male)')
plt.show()

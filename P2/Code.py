import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load dataset
df = pd.read_csv('customer.csv')

# Convert categorical data to numerical
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])  # Male: 1, Female: 0

# Compute Euclidean distance
numeric_data = df[['age', 'income', 'gender']].values
euclidean_distances = pairwise_distances(numeric_data, metric='euclidean')

print("Euclidean Distances:")
print(euclidean_distances)

# Compute Jaccard similarity for categorical data (gender)
gender_data = df[['gender']].values
jaccard_similarity = 1 - pairwise_distances(gender_data, metric='jaccard')

print("Jaccard Similarity:")
print(jaccard_similarity)

# Dissimilarity matrix (1 - similarity)
jaccard_dissimilarity = 1 - jaccard_similarity

print("Jaccard Dissimilarity:")
print(jaccard_dissimilarity)

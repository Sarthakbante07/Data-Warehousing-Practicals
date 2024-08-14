import pandas as pd

# Load datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

# Display the original data
print("Original Data Part 1:")
print(df1)
print("\nOriginal Data Part 2:")
print(df2)

# Handling missing values
# Fill missing 'age' and 'income' with the mean of the column
df1['age'].fillna(df1['age'].mean(), inplace=True)
df1['income'].fillna(df1['income'].mean(), inplace=True)

# Fill missing 'gender' with the mode of the column
df1['gender'].fillna(df1['gender'].mode()[0], inplace=True)

# Display cleaned data
print("\nCleaned Data Part 1:")
print(df1)




# Concatenate the datasets
df = pd.concat([df1, df2], ignore_index=True)

# Display integrated data
print("\nIntegrated Data:")
print(df)

df.shape

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

df.info()

print("Is there are any missing values:",df.isnull().values.any())

df.isnull().sum()

sns.heatmap(df.isnull())

missing_percent = df.isnull().sum() * 100 /len(df)


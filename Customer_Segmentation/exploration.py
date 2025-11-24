df.info()

print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

print("\nSummary Statistics:")
display(df.describe())
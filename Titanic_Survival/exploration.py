df.shape
df.info()
df.describe().style.background_gradient(cmap='viridis')
sns.countplot(x='Survived', color='orange', data=df)
sns.countplot(x='Sex', hue='Survived', data=df)
df.isnull().sum()

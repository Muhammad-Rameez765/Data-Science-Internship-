df_n = df.dropna(axis=0)

print("Is now there are any missing values:",df_n.isnull().values.any())

sns.heatmap(df_n.isnull())

df_n.duplicated()

df_n.describe().style.background_gradient(cmap='viridis')

df_n.describe(include='all').style.background_gradient(cmap='viridis')

df_n[df_n['Runtime (Minutes)']>= 180]

df_n[df_n['Runtime (Minutes)'] >= 180]['Title']



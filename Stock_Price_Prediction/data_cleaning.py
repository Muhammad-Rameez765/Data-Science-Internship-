df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)
print(df.isnull().sum())

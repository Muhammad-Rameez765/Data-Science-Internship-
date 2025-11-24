df_n.groupby('Year')['Votes'].mean().sort_values(ascending = False)

df_n.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending = False)

df_n.groupby('Director')['Rating'].mean().sort_values(ascending = False)

top_10 = df_n.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']]

df_n['Year'].value_counts()

df_n.groupby('Year')['Rating'].mean().sort_values(ascending=False)
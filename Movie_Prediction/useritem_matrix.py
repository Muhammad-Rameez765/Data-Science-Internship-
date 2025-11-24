user_item = df.pivot_table(values='Rating', index='Rank', columns='Title').fillna(0)
user_item.shape


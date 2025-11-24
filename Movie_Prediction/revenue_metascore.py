df_cleaned = df.dropna(subset=['Rating', 'Votes', 'Revenue (Millions)', 'Metascore'])

# Feature Engineering for 'Genre': One-Hot Encode the top 10 most frequent genres
genre_counts = df_cleaned['Genre'].str.split(',').explode().str.strip().value_counts()
top_10_genres = genre_counts.head(10).index.tolist()

for genre in top_10_genres:
    # Create a binary column (1 if the movie has this genre, 0 otherwise)
    df_cleaned[genre] = df_cleaned['Genre'].apply(lambda x: 1 if isinstance(x, str) and genre in x else 0)

# Select features and target
features = ['Votes', 'Runtime (Minutes)', 'Year', 'Revenue (Millions)', 'Metascore'] + top_10_genres
target = 'Rating'

X = df_cleaned[features]
y = df_cleaned[target]

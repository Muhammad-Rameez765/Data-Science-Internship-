true_ratings = []
pred_ratings = []

for _, row in test.iterrows():
    user = row['Rank']
    movie = row['Title']
    true = row['Rating']
    if user in pred_df.index and movie in pred_df.columns:
        pred = pred_df.loc[user, movie]
        true_ratings.append(true)
        pred_ratings.append(pred)

rmse = np.sqrt(mean_squared_error(true_ratings, pred_ratings))
rmse
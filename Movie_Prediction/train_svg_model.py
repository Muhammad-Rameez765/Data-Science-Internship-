svd = TruncatedSVD(n_components=50, random_state=42)
matrix = user_item.values
svd_matrix = svd.fit_transform(matrix)
reconstructed = np.dot(svd_matrix, svd.components_)
pred_df = pd.DataFrame(reconstructed, index=user_item.index, columns=user_item.columns)
pred_df.head()


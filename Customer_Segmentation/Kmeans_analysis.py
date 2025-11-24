kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

df['Cluster'] = y_kmeans

print("\n KMeans Clustering Completed!")
print(df.head())

kmeans.predict([[15, 39]])
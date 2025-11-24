sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

sns.pairplot(df, diag_kind='kde')
plt.suptitle('Pairwise Relationships', y=1.02)
plt.show()

num_cols = df.select_dtypes(include=['number']).columns
for col in num_cols:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col], color='skyblue')
    plt.title(f'Boxplot for {col}')
    plt.show()
    

plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'purple']

for i in range(5):
    plt.scatter(X_scaled[y_kmeans == i, 0], X_scaled[y_kmeans == i, 1],
                s=80, c=colors[i], label=f'Cluster {i+1}')

# Plot centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=250, c='cyan', marker='D', label='Centroids')

plt.title('Customer Segments based on Income & Spending Score')
plt.xlabel('Annual Income (scaled)')
plt.ylabel('Spending Score (scaled)')
plt.legend()
plt.show()


plt.figure(figsize=(8,5))
sns.countplot(x='Cluster', data=df, palette='Set2')
plt.title('Customer Count per Cluster')
plt.show()


#3D Visualization
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Age'], df['Annual Income (k$)'], df['Spending Score (1-100)'],
           c=df['Cluster'], cmap='viridis', s=60)

ax.set_xlabel('Age')
ax.set_ylabel('Annual Income (k$)')
ax.set_zlabel('Spending Score (1-100)')
ax.set_title('3D Visualization of Customer Clusters')
plt.show()
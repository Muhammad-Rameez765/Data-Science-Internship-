cluster_summary = df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)', 'Age']].mean()
print("\n📊 Cluster Characteristics:\n")
display(cluster_summary)

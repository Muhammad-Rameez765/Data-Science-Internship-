sns.barplot(x='Year', y='Votes', data = df_n)
plt.title("Voting By Year")


sns.barplot(x='Year', y='Revenue (Millions)', data = df_n)
plt.title("Revenue By Year")


sns.barplot(x=top_10['Runtime (Minutes)'],y=top_10['Title'], color='gold')
plt.title('Top 10 Lengthly Movies')


sns.scatterplot(x='Rating',y='Revenue (Millions)',color='orange', data=df_n)


feature_importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.title('Feature Importance for Rating Prediction')
plt.xlabel('Importance Score')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Feature importance plot saved as 'feature_importance.png'")

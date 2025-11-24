X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1, max_depth=10)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
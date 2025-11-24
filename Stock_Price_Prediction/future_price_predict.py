last_60_days = scaled_data[-60:]
future_input = np.array([last_60_days])
future_pred = model.predict(future_input)
predicted_price = scaler.inverse_transform(
    np.concatenate((np.zeros((1,3)), [[future_pred[0][0]]], np.zeros((1,1))), axis=1)
)[0,3]
print(f"Predicted next day closing price: {predicted_price}")
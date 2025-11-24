data = df[['open', 'high', 'low', 'close', 'volume']]

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)


X, y = [], []
sequence_length = 60

for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i])  # last 60 days
    y.append(scaled_data[i, 3])  # next day's close (index 3)

X, y = np.array(X), np.array(y)
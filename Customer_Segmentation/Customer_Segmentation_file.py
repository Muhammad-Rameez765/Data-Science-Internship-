joblib.dump(kmeans, "Customer_Segmentation")


model = joblib.load("Customer_Segmentation")
model.predict([[15, 39]])
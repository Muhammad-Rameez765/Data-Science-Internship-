# Summary of Data Science Internship Projects at ArchTechnologies

## 1. Task 1: Titanic Survival Prediction (Classification)
**Problem Type:** Binary Classification  
**Model Used:** Logistic Regression  
**Goal:** Predict whether a passenger survived based on features like Gender, Age, Passenger Class (PClass), and Fare.

**Key Result:** Achieved approximately **78.3% accuracy**.  
**Key Findings:**  
- Gender was the most significant predictor (females had higher survival rates).  
- Passenger Class strongly impacted likelihood of survival (1st-class passengers survived more often).

---

## 2. Task 2: Stock Price Prediction (Time Series Forecasting)
**Problem Type:** Time Series Regression  
**Model Used:** LSTM Neural Network (Long Short-Term Memory)  
**Goal:** Predict the next day's closing stock price using sequences of historical OHLCV data (Open, High, Low, Close, Volume).

**Key Result:** Successfully predicted next-day closing price.  
**Performance Evaluation:**  
- Mean Squared Error (MSE)  
- R² Score

---

## 3. Task 3: Customer Segmentation (Unsupervised Learning)
**Problem Type:** Unsupervised Clustering  
**Model Used:** K-Means Clustering  
**Goal:** Segment retail customers using Age, Annual Income, and Spending Score.

**Methodology:**  
- Optimal number of clusters determined using the **Elbow Method** → **k = 5**

**Key Result:** Identification of **5 distinct customer segments**, such as:  
- High-income Luxury Spenders  
- Budget-conscious Shoppers  
- High-income Careful Spenders  

---

## 4. Task 4: IMDB Movie Rating Predictor (Regression)
**Problem Type:** Regression  
**Model Used:** Random Forest Regressor  
**Goal:** Predict final IMDB Rating using Votes, Metascore, Revenue (Millions), Runtime, and Genre.

**Key Results:**  
- **R² = 0.7410**  
- **RMSE = 0.4312**

**Feature Importance:**  
- Votes and Metascore were the most influential features.

---

# Technologies Used

### Core Languages
- Python  

### Data Manipulation & Analysis
- pandas  
- NumPy  

### Visualization
- Matplotlib  
- Seaborn  

### Machine Learning (Traditional)
- scikit-learn  

### Deep Learning (Time Series)
- TensorFlow / Keras (LSTM)


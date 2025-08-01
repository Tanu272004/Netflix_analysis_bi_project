import pandas as pd
import numpy as np
from Netflix2 import Faker
import random
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Initialize Faker for synthetic data generation
fake = Faker()

# Step 1: Generate synthetic Netflix-like dataset
num_rows = 5000
years = np.random.randint(2000, 2023, size=num_rows)
genres = ['Drama', 'Comedy', 'Action', 'Documentary', 'Thriller', 'Romance', 'Horror', 'Sci-Fi']
ratings = ['G', 'PG', 'PG-13', 'R', 'TV-MA']
countries = ['United States', 'India', 'United Kingdom', 'Canada', 'Australia', 'Japan']

data = {
    'title': [fake.sentence(nb_words=3) for _ in range(num_rows)],
    'release_year': years,
    'genre': [random.choice(genres) for _ in range(num_rows)],
    'country': [random.choice(countries) for _ in range(num_rows)],
    'rating': [random.choice(ratings) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

# Save the dataset
dataset_path = r'T:\python\JARVIS\netflix_dataset.csv'
df.to_csv(dataset_path, index=False)
print(f"Netflix dataset created at: {dataset_path}")

# Step 2: Group data by year for forecasting
yearly_data = df.groupby('release_year').size().reset_index(name='count')

# Prepare data for ML
X = yearly_data[['release_year']]
y = yearly_data['count']

# Step 3: Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict next 5 years
future_years = np.array(range(2023, 2028)).reshape(-1, 1)
predictions = model.predict(future_years)

# Create forecast DataFrame
forecast_df = pd.DataFrame({
    'release_year': future_years.flatten(),
    'predicted_titles': predictions.astype(int)
})

# Save forecast
forecast_path = r'T:\python\JARVIS\netflix_forecast.csv'
forecast_df.to_csv(forecast_path, index=False)
print(f"Forecast file created at: {forecast_path}")

# Step 4: Visualization
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Actual Titles')
plt.plot(future_years, predictions, color='red', linestyle='--', label='Forecasted Titles')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.title('Netflix Titles Forecast')
plt.legend()
plt.show()
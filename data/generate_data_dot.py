import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random latitudes and longitudes within the approximate range of Portugal's mainland
lat_min, lat_max = 37.5, 42.0  # Latitude range for mainland Portugal
lon_min, lon_max = -9.6, -6.0  # Longitude range for mainland Portugal

# Generate 5000 random latitudes, longitudes, and purchases
latitudes = np.random.uniform(lat_min, lat_max, 500)
longitudes = np.random.uniform(lon_min, lon_max, 500)
purchases = np.random.randint(0, 1000, 500)  # Purchases between 0 and 1000

# Create the DataFrame
df = pd.DataFrame({
    'lat': latitudes,
    'lon': longitudes,
    'Purchases': purchases
})

# Display the first few rows of the generated dataset
df.head()
df.to_csv("data_dot_map.csv")
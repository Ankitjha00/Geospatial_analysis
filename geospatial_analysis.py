import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")

# Remove missing latitude/longitude
df = df.dropna(subset=['Latitude', 'Longitude'])

# Scatter plot for locations
plt.figure(figsize=(10,6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)
plt.title("Geographical Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Top cities
top_cities = df['City'].value_counts().head(10)
print("\nTop 10 Cities:")
print(top_cities)

plt.figure(figsize=(8,5))
sns.barplot(x=top_cities.values, y=top_cities.index)
plt.title("Top 10 Cities with Highest Number of Restaurants")
plt.show()

# Country distribution
print("\nCountry Code Distribution:")
print(df['Country Code'].value_counts().head(10))

# Correlation
corr = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Between Location and Rating")
plt.show()

# Conclusion:
# - Restaurants are concentrated in specific cities
# - Location has weak correlation with ratings

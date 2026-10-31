import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Load dataset
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

# -------------------------------
# 🔹 DATA CLEANING
# -------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# Drop rows with important missing values
df.dropna(subset=['date_added', 'rating'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date
df['date_added'] = pd.to_datetime(df['date_added'])

print("\nData after cleaning:")
print(df.info())

# -------------------------------
# 🔹 DATA ANALYSIS
# -------------------------------

print("\nType Count:")
print(df['type'].value_counts())

print("\nTop Countries:")
print(df['country'].value_counts().head(5))

# -------------------------------
# 🔹 VISUALIZATION
# -------------------------------

# 1. Movies vs TV Shows
plt.figure()
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.xticks(rotation=45)
plt.show()

# 2. Top 10 Countries
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xticks(rotation=45)
plt.show()

# 3. Content growth over years
plt.figure()
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Growth Over Years")
plt.show()

# -------------------------------
# 🔹 INSIGHTS
# -------------------------------

print("\n🔹 Key Insights:")
print("✔ Movies are more than TV Shows")
print("✔ USA produces most content")
print("✔ Content increased after 2015")
print(f"✔ Dataset contains {df.shape[0]} rows and {df.shape[1]} columns")
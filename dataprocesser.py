import pandas as panda
movies = panda.read_csv("movies.csv")
# analyse the data within the csv
print("\nSum of Missing Values")
print(movies.isnull().sum())
print("\nThe First 5 Movies")
print(movies.head())
print("\nMovies Information")
print(movies.info())
print("\nMovies Statistics")
print(movies.describe())
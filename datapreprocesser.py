import pandas as panda
movies = panda.read_csv("movies.csv")
movies = movies[["title", "release_date", "genres", "budget", "revenue"]]
print(movies.columns[movies.columns.duplicated()].tolist())
# analyse the data within the csv
print("\nSum of Missing Values")
print(movies.isnull().sum())
print("\nThe First 5 Movies")
print(movies.head())
print("\nMovies Information")
print(movies.info())
print("\nMovies Statistics")
print(movies.describe())

# clean up section
# checking for duplicate rows
print("\nDuplicate Movie Entries")
print(movies.duplicated().sum())

# then we remove duplicate movie rows
movies = movies.drop_duplicates()
# then check again to see if any were missed
print("\nDuplicate Movie Entries Check")
print(movies.duplicated().sum())
# save new cleaned data set
movies.to_csv("movies.csv", index=False)

# now we want to remove any entries with missing revenue or budget fields
movies = movies.dropna(subset=["budget", "revenue"])
movies = movies[movies["revenue"]!=0]
movies = movies[movies["budget"]!=0]
print("\nMovies Count After Cleaning")
print(len(movies))
# save cleaned set
movies.to_csv("movies.csv", index=False)

#extract fields we need, starting with turning date into just year
movies["release_date"] = panda.to_datetime(movies["release_date"])
movies["release_year"] = movies["release_date"].dt.year
# update the dataset with a new field
movies.to_csv("movies.csv", index=False)

# convert movie genres into true or false fall in categories
genre_columns = movies["genres"].str.get_dummies(sep=", ")
# add new columns of T/F to our existing dataset
movies = panda.concat([movies, genre_columns], axis=1)
movies.to_csv("movies.csv", index=False) #save

# titles for graph visualisation
movietitles = movies["title"]
# the features for our regression model
x_value = movies[["budget", "release_year"] + list(genre_columns.columns)]
# what I want to predict
y_value = movies["revenue"]
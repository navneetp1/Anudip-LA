import pandas as pd

# step 1: read the csv file using pandas
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = pd.read_csv(r'C:\Python Programs\assignment\movie_metadata.csv', dtype=None)
# clean_data = data.dropna()

# print(data)
# print(clean_data)

# step 2: we can go 2 ways, depending on the employer's requirements, we can either remove the rows that have NaN data or just rmeove the entire row itself

# approach one
# replacing the NaN values with some specific text, or you can use the ffill() method which fills by looking around the neighboring rows..
# dataFrame.ffill(inplace=True)
# OR
# dataFrame.fillna(value="-",inplace=True)


# approach two 
# remove the rows with NaN values

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
dataFrame = pd.DataFrame(data)
dataFrame.dropna(inplace=True)

movies = dataFrame['movie_title'] 

movies = movies.str.replace("\xa0","")

# print(dataFrame)

# ----------------------------------------------------------------------
# step 4 - unwanted columns

# https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop
first_row = dataFrame.columns.tolist()
print(first_row)

for att,data in enumerate(first_row):
    print(f"{chr(att+65)} - {data}")

print("\n\n================================\n\n")


dataFrame.drop(labels=first_row[2:8],axis=1, inplace=True)

new_row = dataFrame.columns.tolist()
for att,data in enumerate(new_row):
    print(f"{chr(att+65)} - {data}")

print()

# print(dataFrame)



import numpy as np

movie_arr = np.array(movies)
director = np.array(dataFrame['director_name'])
scores = np.array(dataFrame['imdb_score'])
year = np.array(dataFrame['title_year'])

# print(movie_arr)
# print(director)
# print(scores)


james_movies = np.array(movie_arr[np.where(director == "James Cameron")])
movie_years = np.array(year[np.where(director == "James Cameron")])
james_rating = np.array(scores[np.where(director == "James Cameron")])

sorted = np.argsort(james_rating)

james_movies = james_movies[sorted]
movie_years = movie_years[sorted]
james_rating = james_rating[sorted]

print(james_movies, james_rating)

james_movies_with_years = [f"{movie} ({int(year)})" for movie, year in zip(james_movies, movie_years)]


import matplotlib.pyplot as plt

color_palette = ["#00c04b", "#1fd655", "#39e75f", "#5ced73", "#83f28f", "#abf7b1", "#cefad0"]

hbar = plt.barh(james_movies_with_years, james_rating, color=color_palette[::-1], linewidth=1.5, edgecolor="black")
plt.bar_label(hbar, labels=james_rating, label_type="center", fontsize=10)

plt.xlabel("Movies By James Cameron")
plt.ylabel("IMDB Ratings")
plt.title("Highest Rated Movies By James Cameron")
plt.yticks(rotation=45)


plt.tight_layout()
plt.show()


# filters - genre[Action]Language[Action]Year[2011-2015]Rating[>7]

genres = np.array(dataFrame['genres'])
language = np.array(dataFrame['language'])
release_year = np.array(dataFrame['title_year'])
rating = np.array(dataFrame['imdb_score'])

# these are the list of conditions
is_action = np.char.find(str(genres), "Action") >= 0 
is_english = language == "English"
is_in_year_range = np.logical_and(release_year >= 2011, release_year <= 2015)
has_high_rating = rating >= 7

valid_indexes = np.where(is_action & is_english & is_in_year_range & has_high_rating)[0]

directors = director[valid_indexes]
movies_list = movie_arr[valid_indexes]

print("\nAction movies made in English, released b/w 2011 and 2015 and has a rating >= 7")
# for dir,mov in zip(directors, movies_list):
#     print(f"Director: {dir} | Movie: {mov} \n")

filtered = pd.DataFrame({
    "Director":james_movies,
    "Movie": movie_years
})

print(filtered)

filtered.to_excel("Filtered Data.xlsx",index=False)













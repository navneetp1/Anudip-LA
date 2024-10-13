# https://www.kaggle.com/datasets/karrrimba/movie-metadatacsv
import pandas as pd

data = pd.read_csv(r"C:\Python Programs\assignment\movie_metadata.csv")
data = data.dropna()

print(data)


titles = data['movie_title']
pure_titles = titles.str.replace("Â","")

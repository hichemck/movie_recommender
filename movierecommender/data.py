import pandas as pd

ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
ratings = ratings.pivot(columns='movieId', values='rating', index='userId')

movies = pd.read_csv('./data/ml-latest-small/movies.csv')

sorted_rating_sums = ratings.sum(axis=0).sort_values(ascending=False)
proba_series = sorted_rating_sums / sorted_rating_sums.sum()

users_unseen_films = ratings.T.isna()
"""
Contains various recommondation implementations
"""

import numpy as np
import pandas as pd
from movierecommender.data import ratings, proba_series, users_unseen_films

#from movierecommender.nmf import model, Q, P


def get_unseen_films(user_id):
    user_boolean_series = users_unseen_films[[user_id]]
    unseen_films = user_boolean_series.index[user_boolean_series[user_id]].tolist()
    return unseen_films

def dummy_recommender(user_id, user_item_matrix, k):
    """
    return k random unseen movies for user with user_id
    """
    user_ratings = user_item_matrix.loc[user_id]
    random_movie_ids = user_ratings.loc[user_ratings.isnull()].sample(n=k).index
    return random_movie_ids.values

def popular_films_recommender(user_id, user_item_matrix, k):
    """
    return k random (probabilties proportional to ratings) unseen movies for user with user_id
    """    
    unseen_films_ratings_sums = user_item_matrix.sum(axis=0).loc[get_unseen_films(user_id)]
    proba_series = unseen_films_ratings_sums / unseen_films_ratings_sums.sum()
    return np.random.choice(proba_series.index, p=proba_series.values, size=5)
   

def nmf_recommender(user_id, user_item_matrix, k, model):
    """
    return k highest rated unseen movies as predicted by non negative matrix factorization
    """
    R = user_item_matrix
    R_imputed = user_item_matrix.fillna(0)
    ratings_user = R_imputed.loc[[user_id]]
    query = ratings_user.values
    
    p_user = model.transform(query)
    r_hat_user = model.inverse_transform(p_user)

    r_hat_df = pd.DataFrame(r_hat_user).T
    c = r_hat_df.columns[0]
    final_df = r_hat_df[r_hat_df.index.isin(get_unseen_films(1))].sort_values(by=0,ascending=False)

    output = final_df[:k].index.tolist()    
    
    return output
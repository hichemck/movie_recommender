"""
Contains various recommondation implementations. 

All classes should be derived from the BaseRecommender
"""

import numpy as np
import pandas as pd


class BaseRecommender:
    """
    Recommender interface class
    """

    def __init__(self, X):
        """
        X is the user-item matrix
        """
        self.X = X   


    def recommend(self, user_id, k):
        """
        Give a list of top-k recommondations for a user
        """
        raise NotImplementedError


class DummyRecommender(BaseRecommender):

    def recommend(self, user_id, k):
        """
        Returns k random movies the user hasn't seen yet
        """
        raise NotImplementedError


class GlobalRecommender(BaseRecommender):

       
    def recommend(self, user_id, k):
        """
        Calculates the top-k rated movies that user hasn't seen yet
        """    
        raise NotImplementedError




if __name__ == "__main__":
    pass


import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
from data import ratings
import pickle


R = ratings

R_imputed = R.fillna(0)

model = NMF(n_components=20, init='random', random_state=15, max_iter=1000)

model.fit(R_imputed)

with open('../models/nmf.pickle', 'wb') as f:
    pickle.dump(model, f)

# Q = model.components_  

# P = model.transform(R_imputed)  

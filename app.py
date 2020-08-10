import pickle
from flask import Flask, render_template, request, redirect, url_for
from movierecommender.data import ratings
from movierecommender.recommender_functions import (dummy_recommender, 
                            popular_films_recommender, nmf_recommender,
                            convert_to_title_list)


with open('./models/nmf.pickle', 'rb') as f:
    nmf_model = pickle.load(f)


app = Flask(__name__)


@app.route('/')
def index():
    user_id = request.args.get('user_id')
    if user_id is None:
        output = render_template('index.html')
    else:
        output = redirect(url_for('user', user_id=user_id))
    return output


@app.route('/user/<user_id>')
def user(user_id):
    user_id = int(user_id)
    recommendation = []
    model = request.args.get('model')
    k = request.args.get('k')
    if k is not None :
            k = int(k)
    print(model)

    if model == 'DR':
        recommendation = dummy_recommender(user_id, ratings, k)
        recommendation = convert_to_title_list(recommendation)
    elif model == 'PFR':
        recommendation = popular_films_recommender(user_id, ratings, k)
        recommendation = convert_to_title_list(recommendation)
    elif model == 'NMF':
        recommendation = nmf_recommender(user_id, ratings, k, nmf_model)
        recommendation = convert_to_title_list(recommendation)
    
    ratings_user = ratings.loc[int(user_id)]
    n_ratings = ratings_user.count()
    best_ratings = ratings_user.sort_values(ascending=False).index[:5].values
    best_ratings = convert_to_title_list(best_ratings)

    return render_template(
        'user.html',
        user_id=user_id,
        n_ratings=n_ratings,
        model=model,
        best_ratings=best_ratings,
        recommendation=recommendation,
        k=k)



@app.route('/film/<film_id>')
def film(film_id):
    return render_template('film.html', film_id=film_id)



if __name__ == "__main__":
    app.run(debug=True)
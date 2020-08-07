from flask import Flask, render_template, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
ratings = ratings.pivot(columns='movieId', values='rating', index='userId')

@app.route('/')
def index():
    user_id = request.args.get('user_id')
    if user_id is None:
        return render_template('index.html')
    else: 
        return redirect(url_for('user', user_id=user_id))
    

@app.route('/user/<user_id>')
def user(user_id):
    model = request.args.get('model')
    print(model)
    if model == 'NMF':
        # pick NMF model
        pass
    if model == 'random':
        # pick random model
        pass
    ratings_user = ratings.loc[int(user_id)]
    n_ratings = ratings_user.count()
    best_ratings = ratings_user.sort_values(ascending=False).index[:5].values
    return render_template('user.html', user_id=user_id, n_ratings=n_ratings, model=model, best_ratings=best_ratings)

@app.route('/film/<film_id>')
def film(film_id):
    return render_template('film.html', film_id=film_id)
    


if __name__ == "__main__":
    app.run(debug=True)



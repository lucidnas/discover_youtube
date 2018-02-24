from dyt_app import app
from flask import render_template
import logic


list_of_movies = logic.movie_tiles_info()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Discover Youtube', movies=list_of_movies)
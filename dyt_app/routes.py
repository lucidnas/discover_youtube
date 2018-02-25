from dyt_app import app
from flask import render_template
import logic


list_of_movies = logic.movie_tiles_info()
print list_of_movies

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Discover Youtube', movies=list_of_movies)

@app.route('/movie/<movie_title>')
def movie_page(movie_title):
    return render_template('movie_page.html', movie_title=movie_title, movie_poster='', movie_trailer='')


from dyt_app import app
from flask import render_template, request
import json, requests
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    query = StringField('query', validators=[DataRequired()], default="")



MOVIE_DATA = json.load(open("data.json"))

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
@app.route('/index')
def home_page():
    searchform = SearchForm()
    return render_template('home_page.html', title='Discover Youtube', movies=MOVIE_DATA, form=searchform)

@app.route('/movie/<movie>')
def movie_page(movie):
    searchform = SearchForm()
    return render_template('movie_page.html', movie=MOVIE_DATA[movie], form=searchform)

@app.route('/search')
def search_page():
    searchform = SearchForm()
    movies_info = {}
    query = request.args.get("query")
    for movie,info in MOVIE_DATA.iteritems():
        if query.lower() in MOVIE_DATA[movie]['title'].lower():
            movies_info[movie]=info
    
    if len(movies_info) == 0 or query.lower() == "":
        return render_template('search_page_not_found.html', form=searchform)
    else: 
        return render_template('search_page.html', title='DYT - Movie Search', movies_info=movies_info, form=searchform, movie_count=len(movies_info))

@app.route('/movies/<genre>')
def movies_page(genre):
    searchform = SearchForm()
    print genre
    movie_genre = {}
    for movie,info in MOVIE_DATA.iteritems():
        if genre.lower() in MOVIE_DATA[movie]['genre'].lower():
            movie_genre[movie]=info
    
    if genre.lower() == "allmovies":
        return render_template('movies_page.html', title='DYT - Movies Page', movies=MOVIE_DATA, form=searchform)
    else:
        return render_template('movies_page.html', title='DYT - Movies Page', movies=movie_genre, form=searchform)

def contact_page():
    pass


from dyt_app import app
from flask import render_template
import json

movie_data = json.load(open("data.json"))

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('home_page.html', title='Discover Youtube', movies=movie_data)

@app.route('/movie/<movie>')
def movie_page(movie):
    return render_template('movie_page.html', movie=movie_data[movie])

@app.route('/search/<input>')
def search_page(input):
    pass

def about_page():
    pass

def contact_page():
    pass


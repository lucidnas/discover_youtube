from dyt_app import app
from flask import render_template

#list_of_movies = logic.movie_tiles_info()
#print list_of_movies

movies_list = {"spiderman" : {
    'poster': u'https://image.tmdb.org/t/p/w500/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg',
    'trailer': u'rk-dF1lIbIg',
    'title': u'Spider-Man: Homecoming',
    'ratings': u'98%',
    'cast': u'stars'
  }, 
  "despicableme3" : {
    'poster': u'https://image.tmdb.org/t/p/w500/5qcUGqWoWhEsoQwNUrtf3y3fcWn.jpg',
    'trailer': u'xM0ODz7v0Rw',
    'title': u'Despicable Me 3'
  },
  "annabelle" : {
    'poster': u'https://image.tmdb.org/t/p/w500/tb86j8jVCVsdZnzf8I6cIi65IeM.jpg',
    'trailer': u'KisPhy7T__Q',
    'title': u'Annabelle: Creation'
  }
}


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('home_page.html', title='Discover Youtube', movies=movies_list)

@app.route('/movie/<movie>')
def movie_page(movie):
    return render_template('movie_page.html', movie=movies_list[movie])

@app.route('/search/<input>')
def search_page(input):
    pass

def about_page():
    pass

def contact_page():
    pass


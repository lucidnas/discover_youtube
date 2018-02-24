import webbrowser

class Movie():
    
    """
    creates Movie objects and stores abstract movie object attributes.
    """
    def __init__(self, movie):
        
        """
        instantiates a movie object with the properties below.
        """
        self.poster = movie['poster']
        self.title = movie['title']
        self.trailer = movie['trailer']

    def show_trailer(self):
        
        """
        a method to play a trailer of a movie via a web browser.
        """
        webbrowser.open(self.trailer)
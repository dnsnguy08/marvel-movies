import webbrowser


class Movie():
    ''' This class stores movie related attributes that are assigned for each
    instance of the class.'''

    def __init__(self, movie_title, poster_image_url, trailer_url):
        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    ''' Open movie trailer in a web browser'''
    def show_trailer(self):
        webbrowser.open(self.trailer_url)

import webbrowser

class Movie():
	''' This class stores movie related information. '''
	
	def __init__(self, movie_title, poster_image_url, trailer_url):
		self.movie_title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_url)


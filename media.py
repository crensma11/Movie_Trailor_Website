"""Defines the Movie class that contains the details of a movie."""
import webbrowser


class Movie():
    """This class provides a way to store movie related information.
        Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the storyline of the movie.
        poster_image_url: A string to store the URL of the movie poster image.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        release_date: A string to store the release date of the movie.
        rating: A string to store the rating of the movie.
    """

    def __init__(
                self, movie_title, movie_storyline, poster_image,
                trailer_youtube, movie_release_date, movie_rating):
        """Initialize instance variables of the class Movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.rating = movie_rating

    def show_trailer(self):
        """Plays the movie trailer in a web browser."""
        webbrowser.open(self.trailer_youtube_url)

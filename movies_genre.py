class Movie:

    GENRES = ["Action", "Thriller", "Comedy"]
    movie_count = 0

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_movie_count()
            self.genre = genre
            self.release_date = date
        else:
            print("Movie genre cannot be added to count")

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_movie_count(cls, increment=1):
        cls.movie_count += increment


equalizer = Movie("Action", 2014)
print(Movie.movie_count)
print(equalizer.genre)

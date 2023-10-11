class Movie:

    movie_count = 0

    def __init__(self, date):
        self.increase_movie_count()
        self.release_date = date

    @classmethod
    # Using the class method decorator to access/modify class attributes via class methods
    def increase_movie_count(cls, increment=1):
        cls.movie_count += increment


print(Movie.movie_count)

rush_hour = Movie(2000)
print(Movie.movie_count)

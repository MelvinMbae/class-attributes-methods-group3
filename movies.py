# An example to show how to manipulate our class attributes using instance methods.
class Movie:

    # class attribute
    # used to store number of our purchased movies
    movie_count = 0

    def __init__(self, date):
        #manipulating our class attr using an instance method
        Movie.movie_count += 1
        # date is an instance attribute
        self.date = date


# Count =  0 before any instance is created
# how to access a class attr using the class name
print(Movie.movie_count)

# instance 1
equalizer1 = Movie(2014)

# how to access a class attr using the an instance
# we can access movie_count with dot notation on the instance
print(equalizer1.movie_count)
print(equalizer1.date)

# count is now 1
print(Movie.movie_count)

equalizer2 = Movie(2018)
print(equalizer2.movie_count)
print(Movie.movie_count)


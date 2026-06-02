from abc import ABC, abstractmethod

class Movie:  #A movie object w a title, genre, and status

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.watched = False

    def mark_watched(self):
        self.watched = True

    def get_info(self):
        status = "Watched" if self.watched else "Unwatched"
        return f"{self.title} [{self.genre}] - {status}"

#SINGLETON
class WatchlistManager:

    _instance = None   # holds the instance

    def __new__(cls):
        if cls._instance is None:  # create a new object the very first time
            cls._instance = super().__new__(cls)
            cls._instance._movies = []   # the master movie list
            print("SINGLETON: This is proof the Watchlist was created (first time only).")
        return cls._instance

    def add_movie(self, movie):
        self._movies.append(movie)
        print(f"  Added: '{movie.get_info()}'")

    def get_movies(self):
        return self._movies

    def show_all(self):
        print("WATCHLIST:")
        if not self._movies:
            print("Empty Watchlist")
        for i, movie in enumerate(self._movies, start=1):
            print(f"  {i}. {movie.get_info()}")

#BEHAVIOURAL
class WatchlistIterator:

    def __init__(self, movies, filter_fn=None): #like if you only want scifi, or watched
        self._movies = movies
        self._filter = filter_fn if filter_fn else lambda m: True
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            if self._filter(movie):
                return movie
        raise StopIteration


#Structural
class MovieDecorator(ABC): #base decorator
    def __init__(self, movie):
        self._movie = movie   # the wrapped object

    @property
    def watched(self):
        return self._movie.watched

    @property
    def genre(self):
        return self._movie.genre

    def mark_watched(self):
        self._movie.mark_watched()

    @abstractmethod
    def get_info(self):
        pass


class FavoriteDecorator(MovieDecorator):
    def get_info(self):
        return "⭐ FAVORITE — " + self._movie.get_info()


class HDDecorator(MovieDecorator):
    def get_info(self):
        return self._movie.get_info() + " [HD]"


class NewReleaseDecorator(MovieDecorator):
    def get_info(self):
        return "NEW — " + self._movie.get_info()



#DEMO
def main():
    print("  Movie Watchlist")

    #SINGLETON
    print("APPLICATION OF SINGLETON")
    wl1 = WatchlistManager()
    wl2 = WatchlistManager()
    print(f"wl1 is wl2 → {wl1 is wl2}")

    #ADDING MOVIES IN GENERAL
    print("Adding movies to the world with BASE movie class!!!")
    inception  = Movie("Inception",        "Sci-Fi")
    superbad   = Movie("Superbad",         "Comedy")
    the_matrix = Movie("The Matrix",       "Sci-Fi")
    knives_out = Movie("Knives Out",       "Mystery")
    interstellar = Movie("Interstellar",   "Sci-Fi")

    #DECORATOR
    print("APPLICATION OF DECORATOR")

    fav_superbad = FavoriteDecorator(superbad)
    print(f"  Decorated: {fav_superbad.get_info()}")

    fancy_matrix = HDDecorator(FavoriteDecorator(the_matrix))
    print(f"  Doubly decorated: {fancy_matrix.get_info()}")

    new_interstellar = NewReleaseDecorator(interstellar)
    print(f"  Decorated: {new_interstellar.get_info()}")


    print("Adding movies to the watchlist!")
    wl1.add_movie(inception)
    wl1.add_movie(fav_superbad)
    wl1.add_movie(fancy_matrix)
    wl1.add_movie(knives_out)
    wl1.add_movie(new_interstellar)


    inception.mark_watched()
    knives_out.mark_watched()

    wl1.show_all()

    # ITERATOR (WITH FILTERS TOO)
    print("ITERATOR")

    # only unwatched movies
    print("\n  Unwatched movies:")
    for movie in WatchlistIterator(wl1.get_movies(), filter_fn=lambda m: not m.watched):
        print(f"    → {movie.get_info()}")

    # only Sci-Fi
    print("\n  Sci-Fi movies:")
    for movie in WatchlistIterator(wl1.get_movies(), filter_fn=lambda m: m.genre == "Sci-Fi"):
        print(f"    → {movie.get_info()}")

    # all movies (no filter)
    print("\n  All movies (no filter):")
    for movie in WatchlistIterator(wl1.get_movies()):
        print(f"    → {movie.get_info()}")


if __name__ == "__main__":
    main()

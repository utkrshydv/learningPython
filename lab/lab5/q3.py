class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def find_by_director(self, name):
        print(f'Movies directed by {name}: ')
        for movie in self.movies:
            if movie.director == name:
                print(f'{movie.title}')

    def show_all(self):
        for movie in self.movies:
            print(f'{movie.title}')


m1 = Movie("Inception", "Christopher Nolan", 2010)
m2 = Movie("Interstellar", "Christopher Nolan", 2014)
m3 = Movie("Pulp Fiction", "Quentin Tarantino", 1994)

collection = MovieCollection()
collection.add_movie(m1)
collection.add_movie(m2)
collection.add_movie(m3)

collection.show_all()
collection.find_by_director("Christopher Nolan")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.in_cart = []

    def add_product(self, product):
        self.in_cart.append(product)

    def total_price(self):
        price = 0
        for product in self.in_cart:
            price += product.price
        return price

    def display_items(self):
        for product in self.in_cart:
            print(f'{product.name}')


p1 = Product(name="T-shirt", price=20.0)
p2 = Product(name="Jeans", price=40.0)
p3 = Product(name="Sneakers", price=60.0)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

print(cart.total_price())


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.playlst = []

    def add_song(self, song):
        self.playlst.append(song)

    def play_all(self):
        for song in self.playlst:
            print(f'{song.title} by {song.artist}')

    def remove_song(self, title):
        self.playlst = [song for song in self.playlst if song.title != title]

song1 = Song("Yesterday", "The Beatles")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Imagine", "John Lennon")

# Create a Playlist instance
my_playlist = Playlist()

# Add songs to the playlist
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)

# Play all songs in the playlist
print("Playing all songs:")
my_playlist.play_all()

# Remove a song by title
my_playlist.remove_song("Bohemian Rhapsody")

# Play all songs after removal
print("\nPlaying all songs after removal:")
my_playlist.play_all()

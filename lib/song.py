class Song:
    songs = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_artist_count(self)
        Song.add_to_genre_count(self)

    @classmethod
    def add_song_to_count(cls, song):
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, song):
        if(song.genre not in cls.genres):
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        if(song.artist not in cls.artists):
            cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        if song.genre in cls.genre_count.keys():
            new_count = cls.genre_count[song.genre] + 1
            cls.genre_count.update({song.genre: new_count})
        else:
            cls.genre_count.update({song.genre: 1})

    @classmethod
    def add_to_artist_count(cls, song):
        if song.artist in cls.artist_count.keys():
            new_count = cls.artist_count[song.artist] + 1
            cls.artist_count.update({song.artist: new_count})
        else:
            cls.artist_count.update({song.artist: 1})
import setuptools

from song import Song


class Album:
    def __init__(self, name: str, song: Song):
        self.name = name
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())

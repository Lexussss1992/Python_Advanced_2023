from album import Album
from song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):

        if album in self.albums:

            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album.name)

    def remove_album(self, album_name: str):

        if album.published:

            return "Album has been published. It cannot be removed."

        if album_name not in self.albums:

            return f"Album {album_name} is not found."

    def details(self):

        return f"Band {self.name}" + "\n".join(str(i) for i in self.albums)

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
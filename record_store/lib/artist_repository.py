from lib.artist import Artist

class ArtistRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        return [
            Artist(row["id"], row["artist_name"], row["genre"])
            for row in rows
        ]
    
    def create(self, artist):
        self._connection.execute("INSERT INTO artists (artist_name, genre) VALUES (%s, %s)",
        [artist.artist_name, artist.genre]
        )
        return None
from lib.album import Album

class AlbumRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        return [
            Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            for row in rows
        ]
        
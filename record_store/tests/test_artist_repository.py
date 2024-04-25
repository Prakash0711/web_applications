from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call all
I get all the artists in the artist table
"""

def test_all(db_connection):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store/seeds/record_store.sql")    
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz")
    ]

"""
When I call create
I create a new entry to the artist table
"""

def test_create(db_connection):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store/seeds/record_store.sql")    
    repository = ArtistRepository(db_connection)
    artist = Artist(5, "Drake", "Hip-Hop")
    repository.create(artist)
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Drake", "Hip-Hop")
    ]
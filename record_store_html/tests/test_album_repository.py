from lib.album_repository import AlbumRepository
from lib.album import Album
"""
When I call all
I get all the albums in the album table
"""

def test_all(db_connection):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store/seeds/record_store.sql")    
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]

"""
When I call create
I create an album in the database
and I can see it back in #all
"""

def test_create(db_connection):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store/seeds/record_store.sql")    
    repository = AlbumRepository(db_connection)
    album = Album(None, "In Ear Park", 2008, 1)
    repository.create(album)
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "In Ear Park", 2008, 1)
    ]
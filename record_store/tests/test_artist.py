from lib.artist import Artist
"""
Constructs with an id, artist_name, genre
"""

def test_constructs():
    artist = Artist(1, "testName", "testGenre")
    assert artist.id == 1
    assert artist.artist_name == "testName"
    assert artist.genre == "testGenre"

"""
Artists with idential contents are equal
"""

def test_compares():
    artist1 = Artist(1, "test name", "Pop")
    artist2 = Artist(1, "test name", "Pop")
    assert artist1 == artist2

def test_stringify():
    artist = Artist(1, "test artist", "test genre")
    assert str(artist) == "Artist(1, test artist, test genre)"
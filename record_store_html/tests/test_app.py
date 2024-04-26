from lib.album_repository import AlbumRepository
from playwright.sync_api import Page, expect

"""
When I call GET /albums 
Returns all the albums
"""

def test_get_albums(page, db_connection, web_client):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store_html/seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1989",
        "Title: Waterloo\nReleased: 1974",
        "Title: Super Trouper\nReleased: 1980"
    ])
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)"
        


"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store_html/seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        "title": "In Ear Park",
        "release_year": "2008",
        "artist_id": "1"
    })

    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, In Ear Park, 2008, 1)"

"""
When I call GET /albums 
Returns all the albums
"""

def test_get_artists(db_connection, web_client):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store_html/seeds/record_store.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist(1, Pixies, Rock)\n" \
    "Artist(2, ABBA, Pop)\n" \
    "Artist(3, Taylor Swift, Pop)\n" \
    "Artist(4, Nina Simone, Jazz)" 

"""
When I call POST /artists with artist info
That artist is now in the list in GET /artists
"""

def test_post_artists(db_connection, web_client):
    db_connection.seed("/Users/prakashvijayanath/Projects/web_applications/record_store_html/seeds/record_store.sql")
    post_response = web_client.post("/artists", data={
        "artist_name": "Drake",
        "genre": "Hip-Hop"
    })

    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Artist(1, Pixies, Rock)\n" \
    "Artist(2, ABBA, Pop)\n" \
    "Artist(3, Taylor Swift, Pop)\n" \
    "Artist(4, Nina Simone, Jazz)\n" \
    "Artist(5, Drake, Hip-Hop)"
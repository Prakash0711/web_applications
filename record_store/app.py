import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

# == Your Routes Here ==
@app.route("/albums", methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return '',200


@app.route("/albums", methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(
        [f"{album}" for album in repository.all()]
    )

@app.route("/artists", methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['artist_name'], request.form['genre'])
    repository.create(artist)
    return '',200

@app.route("/artists", methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repository.all()
    )
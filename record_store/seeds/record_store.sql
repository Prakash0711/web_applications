-- Drop tables if they exist
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

-- Drop sequences if they exist
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Create artists table
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL
);

-- Create albums table
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    constraint fk_artist foreign key(artist_id)
    references artists(id) 
    on delete cascade 
);

-- Seed artists table
INSERT INTO artists (id, artist_name, genre)
VALUES
    (1, 'Pixies', 'Rock'),
    (2, 'ABBA', 'Pop'),
    (3, 'Taylor Swift', 'Pop'),
    (4, 'Nina Simone', 'Jazz')
    -- Add more artists here
    ;

-- Seed albums table
INSERT INTO albums (id, title, release_year, artist_id)
VALUES
    (nextval('albums_id_seq'), 'Doolittle', 1989, 1),
    (nextval('albums_id_seq'), 'Surfer Rosa', 1988, 1),
    (nextval('albums_id_seq'), 'Waterloo', 1974, 2),
    (nextval('albums_id_seq'), 'Super Trouper', 1980, 2),
    (nextval('albums_id_seq'), 'Bossanova', 1990, 1),
    (nextval('albums_id_seq'), 'Lover', 2019, 3),
    (nextval('albums_id_seq'), 'Folklore', 2020, 3),
    (nextval('albums_id_seq'), 'I Put a Spell on You', 1965, 4),
    (nextval('albums_id_seq'), 'Baltimore', 1978, 4),
    (nextval('albums_id_seq'), 'Here Comes the Sun', 1971, 4),
    (nextval('albums_id_seq'), 'Fodder on My Wings', 1982, 4),
    (nextval('albums_id_seq'), 'Ring Ring', 1973, 2)
    ;
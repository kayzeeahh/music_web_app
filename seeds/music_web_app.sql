-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
  );

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
  );

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title1', 2001, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title2', 2002, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title3', 2003, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title4', 2004, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title5', 2005, 5);

INSERT INTO artists (name, genre) VALUES ('Artist1', 'Genre1');
INSERT INTO artists (name, genre) VALUES ('Artist2', 'Genre2');
INSERT INTO artists (name, genre) VALUES ('Artist3', 'Genre3');
INSERT INTO artists (name, genre) VALUES ('Artist4', 'Genre4');
INSERT INTO artists (name, genre) VALUES ('Artist5', 'Genre5');
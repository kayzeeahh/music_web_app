from lib.artist_repository import *

def test_all_artists(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == "Artist1, Artist2, Artist3, Artist4, Artist5"
    
def test_create_an_artist(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, 'Artist6', 'Genre6')
    repository.create(artist)
    assert repository.all() == "Artist1, Artist2, Artist3, Artist4, Artist5, Artist6"
    
    
    
    
    
   
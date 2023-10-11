from lib.artist import *   

"""
test the contruct/initialisation
"""
    
def test_contruct():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"
    
def test_eq():
    artist_1 = Artist(1, "Test Artist", "Test Genre")
    artist_2 = Artist(1, "Test Artist", "Test Genre")
    assert artist_1 == artist_2
    
def test_repr():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.name
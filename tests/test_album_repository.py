from lib.album_repository import *

"""
get all albums
"""
def test_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Title1', 2001, 1),
        Album(2, 'Title2', 2002, 2),
        Album(3, 'Title3', 2003, 3),
        Album(4, 'Title4', 2004, 4),
        Album(5, 'Title5', 2005, 5)
    ]

    """
    call the create method
    a new album is created in the database
    """
    
def test_create(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Title6', 2006, 6)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Title1', 2001, 1),
        Album(2, 'Title2', 2002, 2),
        Album(3, 'Title3', 2003, 3),
        Album(4, 'Title4', 2004, 4),
        Album(5, 'Title5', 2005, 5),
        Album(6, 'Title6', 2006, 6)
        ]
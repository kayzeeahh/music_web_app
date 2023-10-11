# Tests for your routes go here

# === Example Code Below ===
"""
GET /albums
returs a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode ('utf-8') == ""\
        "Album(1, Title1, 2001, 1)\n"\
        "Album(2, Title2, 2002, 2)\n"\
        "Album(3, Title3, 2003, 3)\n"\
        "Album(4, Title4, 2004, 4)\n"\
        "Album(5, Title5, 2005, 5)"
    



'''
POST /albums with album info
info goes into GET/albums list
'''
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/albums",data={
        'title': 'Title6',
        'release_year': '2006',
        'artist_id': '6'
    } )
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ''\
        "Album(1, Title1, 2001, 1)\n"\
        "Album(2, Title2, 2002, 2)\n"\
        "Album(3, Title3, 2003, 3)\n"\
        "Album(4, Title4, 2004, 4)\n"\
        "Album(5, Title5, 2005, 5)\n"\
        "Album(6, Title6, 2006, 6)"
        
        
def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode ('utf-8') == ""\
        "You need to submit a title, release_year and artist_id"
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
    "Album(1, Title1, 2001, 1)\n"
    "Album(2, Title2, 2002, 2)\n"
    "Album(3, Title3, 2003, 3)\n"
    "Album(4, Title4, 2004, 4)\n"
    "Album(5, Title5, 2005, 5)"
)
    
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode ('utf-8') == "Artist1, Artist2, Artist3, Artist4, Artist5"
    
    
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Artist6',
        'genre': 'Genre6'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''
    
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Artist1, Artist2, Artist3, Artist4, Artist5, Artist6"
# === End Example Code ===

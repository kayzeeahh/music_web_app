from lib.artist import *

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT name FROM artists')
        artists =[]
        for row in rows:
            item = row["name"]
            artists.append(item)
        return ', '.join(artists) 
    
    def create(self, artist):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)", [artist.name, artist.genre])
        return None
    
    
    
    
    
    #[row["name"] for row in rows]
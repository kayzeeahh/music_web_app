{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

POST/albums
    title: string
    release_year: number (str)
    artist_id: numer (str)

GET/albums

2. Create Examples as Tests

POST /albums
title: 'Title1'
release_year: 2001
artist_id: 1
expected response (400 Bad Request)

Get/abums
expected response (200 ok)
Album(1, 'Title!', 2001, 1)

3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /albums
  Expected response (200 OK):
  "1, 'Title!', 2001, 1"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
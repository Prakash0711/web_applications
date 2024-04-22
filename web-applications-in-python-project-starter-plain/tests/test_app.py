# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
GET '/'
"""

def test_chosen_one(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am the chosen one!"

"""
GET wave
"""

def test_wave_david(web_client):
    response = web_client.get("/wave?name=David")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am waving at David"
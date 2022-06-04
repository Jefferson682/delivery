def test_request_return_not_found(client):
    assert client.get("/url_not_exist").status_code == 404
    
    
# def test_request_index(client):
#     assert client.get("/").status_code == 200

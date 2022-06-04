def test_app_is_created(app):
    assert app.name == "delivery.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_return_not_found(client):
    assert client.get("/url_not_exist").status_code == 404

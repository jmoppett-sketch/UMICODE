from umicode.config import load_config


def test_load_default_config():
    config = load_config("config/default.yaml")

    assert config["project"]["name"] == "UMICODE"
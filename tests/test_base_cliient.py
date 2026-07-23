from clients.base_client import BaseClient


def test_base_client_can_be_created():
    client = BaseClient()

    assert client is not None

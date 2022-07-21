import pytest
from src import dog_app as flask_app

@pytest.fixture
def app():
  yield flask_app

@pytest.fixture
def client():
  return flask_app.test_client()
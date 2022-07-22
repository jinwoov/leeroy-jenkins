def test_homepage(app, client):
  res = client.get('/')
  assert res.status_code == 200
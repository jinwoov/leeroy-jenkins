def test_homepage(client):
  res = client.get('/')
  print(res.data)
  assert res.status_code == 200
  assert res.data == b"It's the wild wild west dogworld"
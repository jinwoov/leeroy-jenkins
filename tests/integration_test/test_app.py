
def test_homepage(client):
  res = client.get('/')
  assert res.status_code == 200
  assert res.data == b"It's the wild wild west dogworld"

def test_dogs(client):
  expected_dogs = [{"age": 3, "name": "mochi"}, {"age": 16, "name": "kudo"}, {"age": 1, "name": "Ozzie"}]

  res = client.get('/dogs')
  assert res.status_code == 200
  assert res.json == expected_dogs

def test_random_dogs(client):
  res = client.get('/randomdogs')

  assert res.status_code == 200
  assert res.json == []

def test_addpup(client):
  req_data ={'name': 'gochi'}
  res = client.post('/addpup', json=req_data)

  assert res.status_code == 200
  assert res.json == req_data

  res_after = client.get('/randomdogs')

  assert res_after.status_code == 200
  assert res_after.json == [req_data]
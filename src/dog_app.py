from flask import Flask,jsonify,request

dogs = [{"age": 3, "name": "mochi"}, {"age": 16, "name": "kudo"}, {"age": 1, "name": "Ozzie"}]
random_dogs = []

api = Flask(__name__)

@api.route("/dogs", methods=['GET'])
def get_dogs():
  return jsonify(dogs)

@api.route("/", methods=['GET'])
def home_page():
  return jsonify("It's the wild wild west dogworld")

@api.route("/addpup", methods=['POST'])
def add_dog():
  res = request.json
  random_dogs.append(res)
  return jsonify(res)

@api.route('/randomdogs')
def random_dog():
  return jsonify(random_dogs)

if __name__ == "__main__":
  api.run(port=1234, debug=True)
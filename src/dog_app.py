from flask import Flask,jsonify

dogs = [{"age": 3, "name": "mochi"}, {"age": 16, "name": "kudo"}, {"age": 1, "name": "Ozzie"}]

api = Flask(__name__)

@api.route("/dogs", methods=['GET'])
def get_dogs():
  return jsonify(dogs)

@api.route("/", methods=['GET'])
def home_page():
  return jsonify("It's the wild wild west dogworld")

if __name__ == "__main__":
  api.run(port=1234)
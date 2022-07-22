from . import bp_flask
from flask import jsonify,request

dogs = [{"age": 3, "name": "mochi"}, {"age": 16, "name": "kudo"}, {"age": 1, "name": "Ozzie"}]
random_dogs = []


@bp_flask.route("/dogs", methods=['GET'])
def get_dogs():
  return jsonify(dogs)

@bp_flask.route("/", methods=['GET'])
def home_page():
  return "It's the wild wild west dogworld"

@bp_flask.route("/addpup", methods=['POST'])
def add_dog():
  res = request.json
  random_dogs.append(res)
  return jsonify(res)

@bp_flask.route('/randomdogs')
def random_dog():
  return jsonify(random_dogs)
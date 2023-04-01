from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"

@app.route('/users', methods=['GET'])
def users():
    ''' Returns the list of users '''
    with open("{}/user/database/users.json".format(database_path), "r") as f:
        users = json.load(f)
    
    resp = make_response(json.dumps(users, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/users/<userid>', methods=['GET'])
def user_data(userid):
    ''' Returns info about a specific user '''
    with open("{}/user/database/users.json".format(database_path), "r") as f:
        users = json.load(f)

    if userid not in users:
        return "Not found"

    return jsonify(users[userid])

@app.route('/users/<username>/lists', methods=['GET'])
def user_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5000, debug=True)

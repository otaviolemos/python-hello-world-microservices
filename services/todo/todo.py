from flask import Flask, jsonify, make_response
import json
import os

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open('{}/todo/database/todo.json'.format(database_path), "r") as jsf:
    todo_list = json.load(jsf)

@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Todo service is up"

@app.route('/todo', methods=['GET'])
def show_lists():
    ''' Displays all the lists '''

    tlists = []
    for username in todo_list:
        for lname in todo_list[username]:
            tlists.append(lname)
    return jsonify(lists=tlists)

@app.route('/todo/<userid>', methods=['GET'])
def user_list(userid):
    ''' Returns a user oriented list '''

    if userid not in todo_list:
        return "No list found"

    return jsonify(todo_list[userid])

if __name__ == '__main__':
    app.run(port=5001, debug=True)

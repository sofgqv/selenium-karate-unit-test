from flask import Flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/printname')
def printname():
    name_arg = request.args.get('name')

    print(name_arg)

    return jsonify(result=name_arg)

if __name__ == "__main__":
    app.run(debug=True, port=7600)
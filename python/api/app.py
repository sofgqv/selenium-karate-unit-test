from flask import Flask
from flask import request, jsonify
#from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/printname')
def printname():
    name_arg = request.args.get('name')

    print(name_arg)

    return jsonify(result=name_arg)

@app.route('/fizzbuzz')
def fizzbuzz():
    i = request.args.get('input')
    i = int(i)
    if i % 15 == 0:
        return jsonify(result="FizzBuzz")
    elif i % 3 == 0:
        return jsonify(result="Fizz")
    elif i % 5 == 0:
        return jsonify(result="Buzz")
    else:
        return jsonify(result=i)

if __name__ == "__main__":
    app.run(debug=True, port=7600)
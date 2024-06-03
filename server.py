from SQLSyntaxer import SQLSyntaxer

from flask import Flask, jsonify

sql_syntaxer = SQLSyntaxer()

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run()
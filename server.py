from SQLSyntaxer import SQLSyntaxer

from flask import Flask, jsonify, request

sql_syntaxer = SQLSyntaxer()

app = Flask(__name__)


@app.route('/get_syntax', methods=['POST'])
def get_syntax():
    text_query = request.json['text']
    return jsonify(text=sql_syntaxer.translate(text_query)), 200


if __name__ == '__main__':
    app.run()

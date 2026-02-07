from flask import Flask, send_from_directory, jsonify
from mongo_client import insert_note, get_random_note

app = Flask(__name__, static_folder='static')

@app.route('/api/receive/<exclude_user:exclude_user>', methods=['GET'])
def receive_note(exclude_user):
    return jsonify(get_random_note(exclude_user))

@app.route('/api/send', methods=['POST'])
def send_note():
    pass


if __name__ == "__main__":
    app.run()

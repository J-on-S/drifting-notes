from flask import Flask, send_from_directory
from mongo_client import insert_note, get_random_note

app = Flask(__name__, static_folder='static')

@app.route('/api/receive/<anon_id>', methods=['GET'])
def receive_note(anon_id):
    return str(get_random_note(anon_id))

@app.route('/api/send', methods=['POST'])
def send_note():
    pass


if __name__ == "__main__":
    app.run()

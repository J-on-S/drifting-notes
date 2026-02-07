from flask import Flask, send_from_directory
from mongo_client import insert_note, get_random_note

app = Flask(__name__, static_folder='static')

@app.route('/api/receive')
def receive_note():
    return "TODO: receive a note"

@app.route('/api/send')
def send_note():
    return "TODO: send a note"

@app.route('/test')
def test_note():
    return str(get_random_note("USER"))

if __name__ == "__main__":
    app.run()

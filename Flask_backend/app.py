from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/api/receive')
def receive_note():
    return "TODO: receive a note"

@app.route('/api/send')
def send_note():
    return "TODO: send a note"

if __name__ == "__main__":
    app.run()

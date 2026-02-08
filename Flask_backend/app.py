from flask import Flask, send_from_directory, jsonify, request, url_for, redirect
from mongo_client import insert_note, get_random_note

app = Flask(__name__, static_folder='static')

app.rout('/')
def redirect_index():
    return redirect('/static/driftingnotes.html')

@app.route('/api/receive/<anon_id>', methods=['GET'])
def receive_note(anon_id):
    note = get_random_note(anon_id)
    response = {
        "message": note['text'],
        "anon_id": note['senderAnonId']
    }
    return jsonify(response)


@app.route('/api/send', methods=['POST'])
def send_note():
    data = request.form
    message = data['message']
    anon_id = data['anon_id']
    insert_note(message, anon_id)
    return "Note sent!"


if __name__ == "__main__":
    app.run()

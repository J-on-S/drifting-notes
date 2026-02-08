from json import loads
from flask import Flask, send_from_directory, jsonify, request, redirect
from mongo_client import insert_note, get_random_note
from bson.json_util import dumps

app = Flask(__name__, static_folder='static')

@app.route('/')
def redirect_index():
    return redirect('/static/driftingnotes.html')


@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('static/images', path)


@app.route('/api/receive/<anon_id>', methods=['GET'])
def receive_note(anon_id):
    note = get_random_note(anon_id)
    if not note:
        return jsonify({"message": "No available notes right now"}), 404
    response = {
        "message": note['text'],
        "anon_id": note['senderAnonId'],
        "url": note.get("music")
    }
    return jsonify(response)


@app.route('/api/send', methods=['POST'])
def send_note():
    data = request.form
    message = data['message']
    anon_id = data['anon_id']
    url = data['url']

    if not message or not anon_id or not url:
        return 'You need to fill in message and url: <br>Please navigate back <a href="/static/sendmessage.html">to send</a>', 400

    note_id = insert_note(message, anon_id, url)
    return redirect('/static/aftersend.html')


if __name__ == "__main__":
    app.run()

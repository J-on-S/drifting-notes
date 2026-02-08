from json import loads
from flask import Flask, send_from_directory, jsonify, request, redirect
from mongo_client import insert_note, get_random_note
from bson.json_util import dumps
from spotify_oembed import spotify_oembed

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
        "music": note.get("music")
    
    }
    return jsonify(response)


@app.route('/api/send', methods=['POST'])
def send_note():
    data = request.form
    message = data['message']
    anon_id = data['anon_id']
    spotify_url = data['spotifyUrl']
    
    insert_note(message, anon_id)
    return "Note sent!"
    if not text or not anon_id:
        return jsonify({"error": "Missing text or anonId"}), 400
    
    music = None
    if spotify_url:
        try:
            o = spotify_oembed(spotify_url)
            music = {
                "provider": "spotify",
                "url": spotify_url,
                "title": o.get("title"),
                "author": o.get("author_name"),
                "thumbnail": o.get("thumbnail_url"),
                "html": o.get("html")
            }
        except Exception:
            return jsonify({"error": "Invalid Spotify link"}), 400

    note_id = insert_note(text, anon_id, music=music)
    return jsonify({"id": str(note_id)}), 201




if __name__ == "__main__":
    app.run()

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/<path:path>")
def send_webpage(path):
    return send_from_directory("../Hack2026_website", path)

if __name__ == "__main__":
    app.run()

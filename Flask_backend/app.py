from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../Hack2026_website')

if __name__ == "__main__":
    app.run()

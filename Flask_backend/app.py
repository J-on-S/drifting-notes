from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

if __name__ == "__main__":
    app.run()

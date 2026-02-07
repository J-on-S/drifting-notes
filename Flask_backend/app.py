from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def simple_index():
    return "<p>Welcome !</p>"

if __name__ == "__main__":
    app.run()

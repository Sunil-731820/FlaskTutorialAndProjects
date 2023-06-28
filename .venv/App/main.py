from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello FLask I Started Working on that!</p>"

@app.route("/hi")
def Hi():
    return "<h1>Hello FLask</h1>"
if __name__ == "__main__":
    app.run()
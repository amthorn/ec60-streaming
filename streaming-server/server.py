from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10555, debug=True)

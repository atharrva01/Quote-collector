from flask import Flask, render_template, request

app = Flask(__name__)
quotes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        with open("file.txt", "a") as f:
            f.write(f"\nthe quote given by user is {request.form['Quote']}, and this is written by {request.form['Author']}\n")

    with open("file.txt", "r") as f:
        quotes = f.readlines()

    return render_template("index.html", quotes=quotes)

app.run(debug=True)

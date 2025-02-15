from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "ScoutHTML"
    return render_template("index.html", user_name=name)

if __name__ == "__main__":
    app.run(debug=True)

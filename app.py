from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("scavengerhunt.html")

@app.route("/missions")
def missions():
    return render_template("missions.html")

if __name__ == "__main__":
    app.run()

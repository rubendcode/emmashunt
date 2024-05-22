from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def scavengerhunt():
    return render_template('scavenger.html')

@app.route('/missions')
def missions():
    return render_template('missions.html')

if __name__ == '__main__':
    app.run(debug=True)

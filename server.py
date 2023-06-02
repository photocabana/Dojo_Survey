from flask import Flask, render_template, session, request

app = Flask(__name__)

app.secret_key="Python is for Winners"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['post'])
def process():
    session.name = request.form["name"]
    session.location = request.form["location"]
    session.language = request.form.getlist("language")
    session.gender = request.form["gender"]
    session.comment = request.form["comment"]
    return render_template('user.html')

if __name__=="__main__":
    app.run(debug=True)

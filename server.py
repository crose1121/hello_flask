from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="Please enter your phrase in the URL above preceeded by a forward slash --> /   (i like the phrase oogabooga but that's just me)", num="Please also enter the number of times you want the phrase to repeat, preceeded by a forward slash --> /")

@app.route('/success')
def success():
    return "SUCCESS!!!!!!"

@app.route('/<string:phrase>/<int:num>')
def hello(phrase,num):
    return render_template("hello.html",phrase=phrase,num=num)

if __name__ == '__main__':
    app.run(debug=True)
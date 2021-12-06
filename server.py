from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="Please enter your phrase in the URL above preceeded by a forward slash --> /   (i like the phrase oogabooga but that's just me)", num="Please also enter the number of times you want the phrase to repeat, preceeded by a forward slash --> /")

@app.route('/success')
def success():
    return "SUCCESS!!!!!!"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



@app.route('/<string:phrase>/<int:num>')
def hello(phrase,num):
    return render_template("hello.html",phrase=phrase,num=num)

if __name__ == '__main__':
    app.run(debug=True)
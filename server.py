from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello From Flask!! This is my very first web server'

@app.route('/success')
def success():
    return "SUCCESS!!!!!!"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return f"Hello {banana}"*num


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello From Flask!! This is my very first web server'

if __name__ == '__main__':
    app.run(debug=True)
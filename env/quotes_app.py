__author__ = 'Steve'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'wow wee'


if __name__ == '__main__':
    app.run(port=5000, debug=True)



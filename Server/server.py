from flask import Flask

app = Flask(__name__)


@app.route('/members')
def members():
    return {'Members': ['John', 'Steve', 'Bill']}


if __name__ == '__main__':
    app.run(debug=True)

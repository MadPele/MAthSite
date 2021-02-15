from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return 'Hello World5!'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

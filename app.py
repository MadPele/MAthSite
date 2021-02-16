from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Pele',
        'title': '1st post',
        'content': '1st post content',
        'date_posted': 'February 6, 2021'
    },
    {
        'author': 'MadPele',
        'title': '2nd post',
        'content': '2nd post content',
        'date_posted': 'February 6, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

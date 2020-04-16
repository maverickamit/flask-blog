from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Amit Ghosh',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 21,2019'
    },
    {
        'author': 'Sumit Ghosh',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

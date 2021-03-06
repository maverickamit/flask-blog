from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '32bf1335b57eb727fe0ed537e5b5ccba'

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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

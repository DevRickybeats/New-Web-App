from flask import Flask
from markupsafe import escape

from flask import url_for
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    with app.app_context():
        url_for('static', filename='style.css')
    return "<p class= 'flow' >Hello, World!</p>"



# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'




@app.route('/index')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World, OMG'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'


# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()
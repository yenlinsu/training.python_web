from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/div/<float:val>/')
def divide(val):
    return "%0.2f divided by 2 is %0.2f" % (val, val / 2)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/blog/entry/<int:id>/', methods=['GET',])
def read_entry(id):
    return "reading entry %d" % id

@app.route('/blog/entry/<int:id>/', methods=['POST', ])
def write_entry(id):
    return 'writing entry %d' % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='John Doe')

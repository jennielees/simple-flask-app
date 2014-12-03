"""Basic Flask application.

  See flask.pocoo.org for much more detail on Flask, or work through
  the Flask Mega Tutorial for an in-depth guided tour:
  http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)  # Initialize the app.


# Define a function that maps to a specific URL.
@app.route('/')
def index():
    return 'Hello'


# Define a function that maps to another URL, and
# loads a HTML file
@app.route('/index')
def index_html():
    return render_template('index.html')


# Define a function that maps to a URL, and incorporates
# a variable in the template
@app.route('/hello')
def hello():
    default_name = "Stranger"
    return render_template('hello.html',
                           name=default_name)


# Define a function that maps to a URL, and takes user input
# in the form of a "slash" URL parameter
# Try going to http://localhost:5000/goodbye/italian
# and http://localhost:5000/goodbye/portuguese
@app.route('/goodbye/<language>')
def goodbye(language):
    phrase = "Goodbye"
    if language == "italian":
        phrase = "Ciao"
    if language == "french":
        phrase = "Au revoir"

    return render_template('goodbye.html',
                           phrase=phrase)


# Define a function that maps to a URL, and takes user input
# in the form of a query-string (?blah=foo&baz=bar) parameter
@app.route('/chocolate')
def chocolate():
    chocolate_type = request.args.get('type')  # GET from the REQUEST arguments
    if chocolate_type is None:
        chocolate_type = 'milk'

    return render_template('chocolate.html',
                           chocolate_type=chocolate_type)


# Define a function that maps to a URL and takes user input
# in the form of a submitted form
@app.route('/wine', methods=['GET', 'POST'])
def wine():
    wine_type = request.form.get('type')

    # Look in the window where you are running app.py to see this message
    print "Wine type submitted was {}".format(wine_type)

    if not wine_type:  # User didn't submit form
        return render_template('wine.html')
    else:
        wines = {
            'red': 'Cabernet Sauvignon',
            'white': 'Chardonnay',
            'fizzy': 'Champagne',
            'pink': 'Rose',
            'non': 'Grape juice'
        }
        # Notice how the keys in this dictionary correspond to the 'value'
        # in the <option> not the text shown. This makes it easy to have
        # human readable text with computer friendly variable values!
        variety = wines.get(wine_type)
        return render_template('wine.html',
                               variety=variety,
                               wine_type=wine_type)


# Define a function that returns JSON data instead of a HTML template
@app.route('/presents.json')
def presents():
    my_wish_list = ['new socks', 'laptop stickers', 'oranges', 'chocolate']
    to_santa = {
        'event': 'Christmas',
        'recipient': 'Santa',
        'wish_list': my_wish_list
    }
    # This is just a python dictionary, nothing special about it
    # We can return it as JSON with one simple trick!
    # This works for almost any Python object, although for complex types
    # like database models, you have to convert them to a dictionary first.
    return jsonify(to_santa)

# Finally, now we have defined what the app can do, we will run it!
app.run()
# Open up http://localhost:5000 in your web browser.

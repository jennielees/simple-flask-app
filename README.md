### Basic Flask app

This repository contains a simple Flask app.

Look inside `app.py` to see what's going on.

To get it running:

```
$ pip install flask
$ python app.py
```

#### Exercises

* Create a form that asks for the user's name and greets them
* Create a JSON endpoint that returns the current time, and a jQuery front-end that inserts it into a HTML page
* Use peewee to combine the above:
  * Record the user's name, time they last visited, and visit count
  * Ask the user to 'log in' with their name and increment the counter
  * Display a greeting and the total number of times they have logged in
  * If the total logins meets some arbitrary thresholds, display different messages

#### Resources

* [What is Flask?](http://pymbook.readthedocs.org/en/latest/flask.html)
* [Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Flask Introduction](http://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822) (with diagrams!)
* [Flask Official Docs](http://flask.pocoo.org/)

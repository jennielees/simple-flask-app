### Basic Flask app

This repository contains a simple Flask app.

Look inside `app.py` to see what's going on.

#### Exercises

* Create a form that asks for the user's name and greets them
* Create a JSON endpoint that returns the current time, and a jQuery front-end that inserts it into a HTML page
* Use peewee to combine the above:
  * Record the user's name, time they last visited, and visit count
  * Ask the user to 'log in' with their name and increment the counter
  * Display a greeting and the total number of times they have logged in
  * If the total logins meets some arbitrary thresholds, display different messages

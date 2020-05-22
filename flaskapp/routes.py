from flask import render_template, url_for, flash, redirect, request
from telegram.ext import Updater
from flaskapp import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title='Contact')

# make a backend route to send the data somewhere (a database, telegram message, etc)


@app.route("/log_response", methods=['GET', 'POST'])
def log_response():
    request_json = request.get_json()

    # do something (send via telegram eventually)

from flask import render_template, flash, redirect, url_for, send_file, make_response
from flaskapp import app

MAIN_SITE = 'https://entredeveloperslab.com'


@app.route("/")
@app.route("/services")
@app.route("/home")
def home():
    return render_template('home.html', home=True)


@app.route("/tune_in")
def tune_in():
    return render_template('tune_in.html', title='Tune-In')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title='Contact')


@app.route("/my_home", methods=['GET', 'POST'])
def my_home():
    return render_template('my_home.html', title='My Home')


@app.route("/leads", methods=['GET', 'POST'])
def leads():
    return render_template('leads.html', title='Leads')


# make a way to apply
@app.route("/apply", methods=['GET', 'POST'])
def apply():
    return render_template('apply.html', title='Apply')

from flask import render_template, flash, redirect
from flaskapp import app


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


# make a backend route to get keywords data for SEO
@app.route("/SEOLab/get_keywords_recommendations")
def get_keywords_recommendations():
    # make sure that it is a valid request --> require last 4 digits of credit card purchase to authenticate
    stuff = ''

from flask import render_template, flash, redirect, url_for, send_file, make_response
from flaskapp import app
import random

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


@app.route("/virgins")
def virgins():
    choices = ['https://www.linkedin.com/in/changhao-leo-wang-50b5b819a/', 'https://www.linkedin.com/in/anthony-petruzziello-8b3196167/'
               'https://www.linkedin.com/in/andrew-caminiti-339a2518b/', 'https://www.linkedin.com/in/perry-guloien-b4746b14b/',
               'https://www.linkedin.com/in/anika-prakash-000410168/', 'https://www.linkedin.com/in/aryaman-k-019379135/']

    url = random.choice(choices)

    return redirect(url)

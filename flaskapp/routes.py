from flask import render_template, url_for, flash, redirect, request
from flaskapp import app
from flaskapp.models import db, LeadModel
import json


@app.route("/")
@app.route("/services")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/tune_in")
def tune_in():
    return render_template('tune_in.html', title='About')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title='Contact')

# make a backend route to send the data somewhere (a database, telegram message, etc)


@app.route("/add_lead", methods=['GET', 'POST'])
def add_lead():
    request_json = request.get_json(force=True)

    # do something (send via telegram eventually)
    try:
        name = request_json['name']
        email = request_json['email']
        phone_number = request_json['phoneNumber']
        subject = request_json['subject']
        message = request_json['message']
    except KeyError:
        return json.dumps({'message': 'Must include mandatory submissions: name, email, phoneNumber, subject, message'}), 401

    # get the optional data
    try:
        additional_platforms = json.dumps(request_json['additionalPlatforms'])
        found_additional_platforms = True
    except KeyError:
        found_additional_platforms = False

    # create a new lead
    new_lead = LeadModel(name=name, email=email, phone_number=phone_number, subject=subject, message=message)

    # add additional platforms if applicable
    if found_additional_platforms:
        new_lead.additional_platforms = additional_platforms

    # add it to the database
    db.session.add(new_lead)
    db.session.commit()

    return json.dumps({'message': f"added {new_lead} to the database"}), 201

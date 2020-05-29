from flask import render_template, flash, redirect, url_for, send_file
from flaskapp import app
from flaskapp.SEOLab.exporter import Exporter
import os
import pdfkit


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


# this just hosts the report for viewing purposes (it will be automatically downloaded as well)
# can just download this report
@app.route("/download_seo_report", methods=['GET', 'POST'])
def download_seo_report():
    exporter = Exporter('SEOLabTemplates/keyword_recommendation.html')

    report = exporter.create_report()

    report_path = url_for('static', filename='SEOLabReports') + os.getcwd()

    # create the pdf and download it
    pdf = pdfkit.from_string(str(report), report_path)

    send_file(pdf)

    return report

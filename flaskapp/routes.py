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


# this just hosts the report for viewing purposes (it will be automatically downloaded as well)
# can just download this report --> open a new tab for each of the reports (but don't switch to them automatically)
# ^ do as much as possible in js
# make the report ID a keyword argument --> the report object will be able to generate information on it
@app.route("/download_seo_report/<endpoint>/<report_id>", methods=['GET', 'POST'])
def download_seo_report(report_id, endpoint):
    import pdfkit
    # eventually this will have less arguments as the API will pull them from the json
    report = Report(report_id, endpoint)

    report_html = render_template(f"SEOLabTemplates/{endpoint}.html", report=report, main_site=MAIN_SITE, for_download=True)

    # create the pdf and download it
    options = {
        'page-size': 'A6',
        'margin-top': '0.1in',
        'margin-right': '0.1in',
        'margin-bottom': '0.1in',
        'margin-left': '0.1in',
    }
    pdf = pdfkit.from_string(report_html, False, options=options)

    # this renders the pdf in the browser
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'

    # this can be changed to "attachment;" for downloading purposes
    response.headers['Content-Disposition'] = f"inline; filename={report.id}.pdf"

    return response
    # return report_html


@app.route("/render_seo_report/<endpoint>/<report_id>", methods=['GET', 'POST'])
def render_seo_report(report_id, endpoint):
    from flaskapp.SEOLab.researcher import Report
    # eventually this will have less arguments as the API will pull them from the json
    report = Report(report_id, endpoint)

    return render_template(f"SEOLabTemplates/{endpoint}.html", report=report, main_site=MAIN_SITE, for_download=False)
    # return report_html

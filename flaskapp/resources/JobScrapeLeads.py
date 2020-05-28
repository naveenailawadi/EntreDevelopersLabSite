from flask import request
from flask_restful import Resource
from flaskapp.models import db, JobScrapeLeadsModel, InternalPasswordModel
import json

# set use constants
MAX_OPEN_LEADS = 100


class JobScrapeLeadResource(Resource):
    # this will get the most recent 100 leads
    def get(self):
        open_leads = [lead.__dict__ for lead in JobScrapeLeadsModel.query.filter_by(contacted=False).limit(MAX_OPEN_LEADS).all()]

        # remove the instance objects
        for lead in open_leads:
            lead.pop('_sa_instance_state')
            date = lead['date_posted']
            lead['date_posted'] = f"{date.day}/{date.month}/{date.year}"

        return {'open_leads': open_leads}, 201

    # this can add new leads if necessary
    def post(self):
        # get the new lead information
        try:
            request_json = json.loads(request.get_json(force=True))
        except TypeError:
            request_json = request.get_json(force=True)

        # get the password (angelos)
        if request_json['password'] != InternalPasswordModel.query.filter_by(use='JobScrapeLeadCreation').first().password:
            return {'message': 'incorrect password'}, 403

        # get the information
        company = request_json['company']
        try:
            url = request_json['url']
        except KeyError:
            url = None
        try:
            location = request_json['location']
        except KeyError:
            location = None

        # check if the company is in the database
        test = JobScrapeLeadsModel.query.filter_by(url=url).filter_by(company=company).first()
        if test:
            return {'message': f"{company} already existed as a job scrape lead."}, 201

        # add the information to the database
        new_lead = JobScrapeLeadsModel(company=company, url=url, location=location)
        db.session.add(new_lead)
        db.session.commit()

        return {'message': f"Added {company} as a new job scrape lead."}, 201

    def delete(self):
        # this doesn't acually delete the entry. instead, it marks the entry as contacted
        try:
            request_json = json.loads(request.get_json(force=True))
        except TypeError:
            request_json = request.get_json(force=True)

        # get the information
        lead_id = request_json['leadId']

        # get the item from the database and update it
        old_lead = JobScrapeLeadsModel.query.filter_by(id=lead_id).first()
        old_lead.contacted = True

        db.session.commit()

        return {'message': f"Marked {old_lead.company} as contacted"}, 201


class FoundCompaniesResource(Resource):
    # this endpoint will get all the found companies (in history)
    def get(self):
        companies = [lead.company for lead in JobScrapeLeadsModel.query.all()]

        return {'leads': companies}, 201


class VerifyPasswordResource(Resource):
    def post(self):
        try:
            request_json = json.loads(request.get_json(force=True))
        except TypeError:
            request_json = request.get_json(force=True)

        # get the entered password
        use_case = request_json['use_case']
        entered_password = request_json['password']

        if len(use_case) == 0:
            return {'message': 'no use case provided'}, 400

        password_query = InternalPasswordModel.query.filter_by(use=use_case).filter_by(password=entered_password).first()

        if password_query:
            return {'message': 'correct password'}, 201
        else:
            return {'message': 'Incorrect password.'}, 403

from flask_restful import Api
from flaskapp import app
from flaskapp.resources.Telegram import TelegramResource
from flaskapp.resources.JobScrapeLeads import JobScrapeLeadResource, FoundCompaniesResource, VerifyPasswordResource
api = Api(app)

# add api endpoints
api.add_resource(TelegramResource, '/api/send_telegram')
api.add_resource(JobScrapeLeadResource, '/api/JobScrapeLead')
api.add_resource(FoundCompaniesResource, '/api/FoundCompanies')
api.add_resource(VerifyPasswordResource, '/api/VerifyPassword')

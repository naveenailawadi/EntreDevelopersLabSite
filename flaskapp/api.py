from flask_restful import Api
from flaskapp import app
from flaskapp.resources.Telegram import TelegramResource
api = Api(app)

# add api endpoints
api.add_resource(TelegramResource, '/api/send_telegram')

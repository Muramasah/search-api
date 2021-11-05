
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.Controllers.Websites import Websites
from src.UseCases.FindWebsitesByQuery import find_websites_by_query
from src.UseCases.IndexWebsite import index_website

app = Flask(__name__)

# Sets development mode, it should be setted from outside to be able to run the
# app in production
app.config.update(
    ENV='development'
)

# Allow cross-origin requests, must be removed for security reasons
CORS(app, resources={r"/search_api/v1/*": {"origins": "*"}})

api = Api(app)

# Bind the controllers to the routes
api.add_resource(Websites,
                 '/search_api/v1/websites',
                 resource_class_args=[index_website, find_websites_by_query])

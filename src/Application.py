
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.Controllers.VisitedSites import VisitedSites
from src.UseCases.GetVisitedSites import find_visited_sites_by_query
from src.UseCases.SaveVisitedSite import save_visited_site

app = Flask(__name__)

# Sets development mode, it should be setted from outside to be able to run the
# app in production
app.config.update(
    ENV='development'
)

# Allow cross-origin requests, must be removed for security reasons
CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

# Bind the controllers to the routes
api.add_resource(VisitedSites, '/api/visited_sites',
                 resource_class_args=[save_visited_site, find_visited_sites_by_query])

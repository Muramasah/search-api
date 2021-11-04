# Controller to handle request over VisitedSite resource

from flask_restful import Resource, reqparse
from src.UseCases.GetVisitedSites import GetVisitedSites
from src.UseCases.SaveVisitedSite import SaveVisitedSite

# Parser for POST requests
post_parser = reqparse.RequestParser(bundle_errors=True)

post_parser.add_argument('text', type=str, required=True)
post_parser.add_argument('url', type=str, required=True)
post_parser.add_argument('title', type=str, required=True)

# Parser for GET requests
get_parser = reqparse.RequestParser(bundle_errors=True)

get_parser.add_argument('query', type=str, required=True)


class VisitedSites(Resource):
    def __init__(self, save_visited_site: SaveVisitedSite, get_visited_sites: GetVisitedSites):
        self.__save_visited_site = save_visited_site
        self.__get_visited_sites = get_visited_sites

    def options(self):
        return {'Allow': 'OPTIONS, GET, POST'}, 200

    def post(self):
        arguments = post_parser.parse_args()

        self.__save_visited_site.execute(arguments)

        return f'Text content from {arguments["title"]} stored successfully', 201

    def get(self):
        arguments = get_parser.parse_args()

        visited_sites = self.__get_visited_sites.execute(arguments)

        print(f'{arguments} /n{visited_sites }')

        visited_site_dtos = []

        return visited_site_dtos, 200

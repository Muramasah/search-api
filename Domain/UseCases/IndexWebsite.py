from Domain.Models.Website import Website
from Domain.Services.SearchEngineService import (SearchEngineService,
                                                 search_engine_service)


class IndexWebsite:
    def __init__(self, search_engine: SearchEngineService):
        self.__search_engine = search_engine

    def execute(self, visited_site_dto: dict):
        # The VisitedSite instation should be in a factory service
        new_website = Website(text=visited_site_dto['text'],
                              url=visited_site_dto['url'],
                              title=visited_site_dto['title']
                              )

        self.__search_engine.index_visited_site(new_website)


index_website = IndexWebsite(search_engine_service)

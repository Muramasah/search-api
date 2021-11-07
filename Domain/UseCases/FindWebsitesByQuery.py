

from Domain.Services.SearchEngineService import (SearchEngineService,
                                                 search_engine_service)


class FindWebsitesByQuery:
    def __init__(self, search_engine: SearchEngineService):
        self.__search_engine = search_engine

    def execute(self, filter_dto: dict) -> list:
        website_dtos = self.__search_engine.find_all_by_query(
            filter_dto['query'])

        return website_dtos


find_websites_by_query = FindWebsitesByQuery(search_engine_service)

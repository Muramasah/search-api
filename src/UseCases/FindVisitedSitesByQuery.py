
from src.Repositories.VisitedSitesInMemoryRepository import (
    VisitedSiteInMemoryRepository, visited_site_in_memory_repository)


class FindVisitedSitesByQuery:
    def __init__(self, visited_site_repo: VisitedSiteInMemoryRepository):
        self.__visited_site_repo = visited_site_repo

    def execute(self, filter_dto: dict) -> list:
        return self.__visited_site_repo.find_all_by_query(filter_dto['query'])


find_visited_sites_by_query = FindVisitedSitesByQuery(
    visited_site_in_memory_repository)

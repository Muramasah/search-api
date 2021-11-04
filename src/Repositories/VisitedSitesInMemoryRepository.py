from src.Models.VisitedSite import VisitedSite


class VisitedSiteInMemoryRepository:
    def __init__(self):
        self._storage = {}

    def put(self, visited_site: VisitedSite):
        self._storage[visited_site.url] = visited_site

    def find_all_by_query(self, query: str):
        print(query)
        return self._storage


visited_site_in_memory_repository = VisitedSiteInMemoryRepository()

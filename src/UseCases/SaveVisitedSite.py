from src.Models.VisitedSite import VisitedSite
from src.Repositories.VisitedSitesInMemoryRepository import (
    VisitedSiteInMemoryRepository, visited_site_in_memory_repository)


class SaveVisitedSite:
    def __init__(self, visited_site_repo: VisitedSiteInMemoryRepository):
        self.__visited_site_repo = visited_site_repo

    def execute(self, visited_site_dto: dict):
        newSite = VisitedSite(text=visited_site_dto['text'],
                              url=visited_site_dto['url'],
                              title=visited_site_dto['title']
                              )

        self.__visited_site_repo.put(newSite)


save_visited_site = SaveVisitedSite(visited_site_in_memory_repository)

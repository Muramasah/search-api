
import os

from src.Models.Website import Website
from whoosh.fields import ID, TEXT, Schema
from whoosh.index import create_in
from whoosh.qparser import QueryParser


class SearchEngineService:
    '''
    This service have two responsibilities: coordinate the usage of Whoosh to
    accomplish domain process, such as indexing and searching, and the
    communication with the infrastructure, in this case, the file system.

    In order to remove the communication with the infrastructure, this service
    should have a dependency with a infrastructure service, like a repository.
    That was not done because it was not necessary for a prove of concept.
    '''

    def __init__(self):
        self.index = self.__create_index()

    def find_all_by_query(self, raw_query: str):
        with self.index.searcher() as searcher:
            query = QueryParser("text", self.index.schema).parse(raw_query)
            results = searcher.search(query)

        return results

    def index_visited_site(self, visited_site: Website):
        writer = self.index.writer()

        writer.add_document(url=visited_site.url,
                            title=visited_site.title,
                            text=visited_site.text)
        writer.commit()

    def __create_index(self):
        schema = Schema(title=TEXT(stored=True),
                        url=ID(stored=True),
                        text=TEXT)

        if not os.path.exists("./index"):
            os.mkdir("./index")

        return create_in('./index', schema)


search_engine_service = SearchEngineService()

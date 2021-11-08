
import os

from Domain.Models.Website import Website
from whoosh.fields import ID, TEXT, Schema
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser


class SearchEngineService:
    '''
    This service have two responsibilities: coordinate the usage of Whoosh to
    accomplish domain process, such as indexing and searching, and the
    communication with the infrastructure, in this case, the file system.

    In order to remove the communication with the infrastructure, this service
    should have a dependency with a infrastructure service, like a repository.
    This was not done because it was not necessary for a prove of concept.
    '''

    def __init__(self):
        self.index = self.__create_index()

    def index_or_updates_visited_site(self, visited_site: Website):
        writer = self.index.writer()
        '''
        "If no existing document matches the unique fields of the document
        you’re updating, update_document acts just like add_document."
        ref:
        https://whoosh.readthedocs.io/en/latest/indexing.html#updating-documents
        '''
        writer.update_document(url=visited_site.url,
                               title=visited_site.title,
                               text=visited_site.text)
        writer.commit()

    def find_all_by_query(self, query: str):
        try:
            searcher = self.index.searcher()
            whoosh_hits = self.__index_search(query, searcher)
            result_dtos = self.__transform_hit_to_result_dto(whoosh_hits)

            return result_dtos
        finally:
            searcher.close()

    def __transform_hit_to_result_dto(self, whoosh_hits):
        result_dtos = []

        for hit in whoosh_hits:
            result_dto = {'title': hit['title'],
                          'url': hit['url']}
            result_dtos.append(result_dto)

        return result_dtos

    def __index_search(self, raw_query, searcher):
        query = QueryParser("text", self.index.schema).parse(raw_query)
        whoosh_hits = searcher.search(query)

        return whoosh_hits

    def __create_index(self):
        schema = Schema(title=TEXT(stored=True),
                        url=ID(stored=True, unique=True),
                        text=TEXT)

        if not os.path.exists("./index"):
            os.mkdir("./index")
            return create_in('./index', schema)

        return open_dir("./index")


search_engine_service = SearchEngineService()

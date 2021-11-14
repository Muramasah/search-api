from unittest import TestCase
from unittest.mock import MagicMock

from Domain.UseCases.FindWebsitesByQuery import FindWebsitesByQuery


class TestFindWebsitesByQuery(TestCase):
    '''Test FindWebsitesByQuery use case'''

    def setUp(self) -> None:
        # If we don't mock the class dependencies we are testing those
        # dependencies as well.
        self.mocked_search_engine = MagicMock()

        self.use_case = FindWebsitesByQuery(self.mocked_search_engine)

        return super().setUp()

    def test_execute_should_return_website_dtos(self):
        # Here there are our "given" inputs
        filter_dto = {'query': 'query'}
        result_dtos = {'title': 'title', 'url': 'url'}
        self.mocked_search_engine.find_all_by_query.return_value = result_dtos

        # "when" this process is executed
        returned_result_dtos = self.use_case.execute(filter_dto)

        # "Then", we are assuring that the repository is called with the query
        self.mocked_search_engine.find_all_by_query.assert_called_with(
            filter_dto['query'])
        # We are assuring that the use case is returning the repository
        # result.
        self.assertDictEqual(returned_result_dtos, result_dtos)

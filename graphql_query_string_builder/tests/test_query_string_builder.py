from unittest import TestCase

from graphql_query_string_builder import Query


class QueryStringBuilderTestCase(TestCase):
    def test_query_string_is_built(self):
        query = Query(foo=['id', 'bar'])
        self.assertEqual(str(query), 'query { foo { id bar }}')

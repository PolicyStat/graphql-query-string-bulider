from unittest import TestCase

from graphql_query_string_builder import Query


class QueryStringBuilderTestCase(TestCase):
    def test_query_string_is_built(self):
        query = Query()
        self.assertEqual(
            query.render_query_string(foo=['id', 'bar']),
            'query { foo { id bar }}',
        )

    def test_camel_case_happens_by_default(self):
        query = Query()
        self.assertEqual(
            query.render_query_string(foo_bar_baz=['id', 'bar']),
            'query { fooBarBaz { id bar }}',
        )

    def test_disabling_camel_case_removes_camel_case(self):
        query = Query(auto_camel_case=False)
        self.assertEqual(
            query.render_query_string(foo_bar_baz=['id', 'bar']),
            'query { foo_bar_baz { id bar }}',
        )

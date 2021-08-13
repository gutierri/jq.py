from unittest import TestCase
from jq import JsonQueryParser


class TestJsonQueryParser(TestCase):
    def setUp(self):
        self.in_source = {
            'results': [
                {'x': 1, 'y': 2},
                {'x': 10, 'y': 20}
            ],
            'pagination': {
                'next': True,
                'prev': False
            }
        }

    def test_basic_query(self):
        self.assertEqual(JsonQueryParser(self.in_source, 'results').dump, [
            {'x': 1, 'y': 2},
            {'x': 10, 'y': 20}
        ])

        self.assertEqual(JsonQueryParser(self.in_source, 'pagination').dump, {
            'next': True,
            'prev': False
        })

    def test_operation_with_lists(self):
        self.assertEqual(JsonQueryParser(self.in_source, 'results[::-1]').dump, [
            {'x': 10, 'y': 20},
            {'x': 1, 'y': 2}
        ])

        self.assertEqual(
            JsonQueryParser(self.in_source, 'results[::-1][0]').dump,
            {'x': 10, 'y': 20}
        )

    def test_qs_dot_notation_dict(self):
        self.assertEqual(
            JsonQueryParser(self.in_source, 'pagination.next').dump, True)

    def test_dot_notation_dict_from_list(self):
        self.assertEqual(
            JsonQueryParser(self.in_source, 'results[::-1][0].x').dump, 10)

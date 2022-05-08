#!/usr/bin/env python3
#
# Copyright (C) 2021 Gutierri Barboza <python+me@gutierri.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>
''' jq.py is a simple json processor and filtering (jq-like) for Pythonists
'''
import re
import sys
import json
import argparse


__version__ = '0.2.1'


class JsonQueryParser:
    ''' Creates a Python object from JSON string and allows accessing the data
    structure through Python dot notation syntax and also using native features
    of such structures.
    '''

    def __init__(self, in_source, query_string):
        self.source = in_source
        self.query_string = query_string

    @staticmethod
    def attr_str_to_token(key):
        ''' Retorna str de uma expressão válida Python
        '''
        detect_access_by_index = re.match(r'([a-zA-Z].+?)(\[.+)', key)

        if not detect_access_by_index:
            return f'["{key}"]'

        token, q_index = detect_access_by_index.groups()

        return f'["{token}"]{q_index}'

    def parser_qs(self):
        ''' Process and transform standard input into a valid Python expression

        Takes user input ``self.query_string`` in "dot notation" format,
        processes that input, and builds a valid expression to access the
        properties of ``self.source``, a native Python data structure
        '''
        py_exp = 'self.source'

        if self.query_string:
            py_exp = py_exp + ''.join([JsonQueryParser.attr_str_to_token(k)
                                       for k in self.query_string.split('.')])
        return py_exp

    @property
    def dump(self):
        ''' Returns the result of ``self.query_string``
        '''
        return eval(self.parser_qs(), {}, {'self': self}) # pylint: disable=W0123


def main(source, query):
    ''' Main function
    '''
    with source as json_data:
        json_doc = json.loads(json_data.read())
    parser = JsonQueryParser(json_doc, query)
    print(json.dumps(parser.dump, sort_keys=True, indent=4))


if __name__ == '__main__':
    CMD_PARSER = argparse.ArgumentParser(
        description=__doc__,
    )
    CMD_PARSER.add_argument('source', nargs='?',
                            type=argparse.FileType(encoding="utf-8"),
                            help='a JSON file',
                            default=sys.stdin)
    CMD_PARSER.add_argument('--query','-q', type=str,
                            help='query filter for json struct, like obj py')
    main(**vars(CMD_PARSER.parse_args()))

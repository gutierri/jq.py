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
'''
jq.py is a simple json processor and filtering (jq-like) for Pythonists
'''
import re
import sys
import json
import argparse


def filter_selected_element(element):
    ''' Assemble the dictionary string, selecting operation objects

    It makes a filter of what is a selection of JSON element and an operation
    in a Python data structure (for example in a list).

    Elements that will make selection, are around strings:

    e.g: x ['element']

    And operating elements are outside a string to be able to execute the
    instruction:

    e.g: x [-1]

    >>> filter_selected_element('element')
    '["element"]'

    >>> filter_selected_element('1:1')
    '[1:1]'
    '''
    return '["{}"]'.format(element) if re.match(r'^[a-zA-Z]', element) \
                                    else '[{}]'.format(element)


def json_processor(json_input, query):
    '''
    Given a JSON entry and a Python Obj-like query, it returns
    the value of the filtered JSON.

    >>> json_processor('{"obj": [{"key": "value"}]}', 'obj')
    [{'key': 'value'}]

    >>> json_processor('{"obj": [{"key": "value"}]}', 'obj.-1')
    {'key': 'value'}

    >>> json_processor('[{"key": "value"}]', '0')
    {'key': 'value'}
    '''
    json_data = json.loads(json_input) # pylint: disable=unused-variable
    if query:
        build_dict_str_template = ''.join(
            [filter_selected_element(element) for element in query.split('.')])
        target = 'json_data' + build_dict_str_template
    else:
        target = 'json_data'
    return eval(target) # pylint: disable=eval-used


def main(source, query):
    ''' Filters the input JSON based on the input obj-like query
    '''
    with source as json_data:
        data = json_processor(json_data.read(), query)
        json.dump(data, sys.stdout, indent=4)


if __name__ == '__main__':
    CMD_PARSER = argparse.ArgumentParser(
        description=__doc__,
    )
    CMD_PARSER.add_argument('source', nargs='?',
                            type=argparse.FileType(encoding="utf-8"),
                            help='a JSON file',
                            default=sys.stdin)
    CMD_PARSER.add_argument('--query', type=str,
                            help='query filter for json struct, like obj py')
    main(**vars(CMD_PARSER.parse_args()))

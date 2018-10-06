#!/usr/bin/python3

'''
Copyright 2018 Gabriel Martins Trettel

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.

This Source Code Form is “Incompatible With Secondary Licenses”, as defined
by the Mozilla Public License, v. 2.0.
'''


class Node():
    _used_node_attr = set()
    _header = { 'name':'VARCHAR',
                'label':'VARCHAR',
                'class':'VARCHAR',
                'visible':'BOOLEAN',
                'labelvisible':'BOOLEAN',
                'height':'DOUBLE',
                'x':'DOUBLE',
                'y':'DOUBLE',
                'width':'DOUBLE',
                'color':'VARCHAR' }

    def __init__(self, attr_dict):
        if self.valid(attr_dict):
            self.__attributes = {key:value for key,value in attr_dict.items()}
            Node._used_node_attr.update(attr_dict.keys())

    def valid(self, attr_dict):
        for attribute in attr_dict.keys():
            if attribute not in Node._header:
                raise ValueError('Trying to add a node with unidentified attributes')
        return True

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__attributes['name'] == other.__attributes['name']
        return self.__attributes['name'] == other

    def __hash__(self):
        return hash(self.__attributes['name'])

    def __str__(self):
        formatter = lambda key: str(self.__attributes[key]) if key in self.__attributes else ""
        return ",".join(formatter(key) for key in Node._header.keys() if key in Node._used_node_attr)

    @classmethod
    def update(cls, new_attr):
        Node._header.update(new_attr)

    @classmethod
    def header(cls):
        return {key:value for key,value in Node._header.items() if key in Node._used_node_attr}

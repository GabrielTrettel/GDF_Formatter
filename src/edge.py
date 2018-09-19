#!/usr/bin/python3

'''
Copyright 2018 Gabriel Martins Trettel

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.

This Source Code Form is “Incompatible With Secondary Licenses”, as defined
by the Mozilla Public License, v. 2.0.
'''

class Edge():
    _used_edge_attr = set()
    _header = { 'node1':'VARCHAR',
                'node2':'VARCHAR',
                'weight':'DOUBLE',
                'directed':'BOOLEAN',
                'color':'VARCHAR' }

    def __init__(self, attr_dict):
        if self.valid(attr_dict):
            self.__attributes = {key:value for key,value in attr_dict.items()}
            Edge._used_edge_attr.update(attr_dict.keys())

    def valid(self, attr_dict):
        for attribute in attr_dict.keys():
            if attribute not in Edge._header:
                raise ValueError('Trying to add a edge with unidentified attributes')
        return True

    def __eq__(self, node):
        return (self.__attributes['node1'] != node.__attributes['node1']) and (self.__attributes['node2'] != node.__attributes['node1'])

    def __hash__(self):
        return hash("".join(str(v) for v in self.__attributes.values()))

    def __str__(self):
        formatter = lambda key: str(self.__attributes[key]) if key in self.__attributes else ""
        return ",".join(formatter(key) for key in Edge._header.keys() if key in Edge._used_edge_attr)

    @classmethod
    def update(cls, new_attr):
        Edge._header.update(new_attr)

    @classmethod
    def header(cls):
        return {key:value for key,value in Edge._header.items() if key in Edge._used_edge_attr}

    def node1(self):
        return self.__attributes['node1']

    def node2(self):
        return self.__attributes['node2']

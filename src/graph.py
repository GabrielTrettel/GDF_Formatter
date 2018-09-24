#!/usr/bin/python3

'''
Copyright 2018 Gabriel Martins Trettel

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.

This Source Code Form is “Incompatible With Secondary Licenses”, as defined
by the Mozilla Public License, v. 2.0.
'''

from node import Node
from edge import Edge


class Graph():
    def __init__(self, custom_nodes=dict(), custom_edges=dict(), allow_equal_edges=False, **kwargs):
        self.__allow_equal_edges = allow_equal_edges
        self.__node_list = set()
        self.__edge_list = set()
        Node.update(custom_nodes)
        Edge.update(custom_edges)
        Node.update(kwargs)

    def validateNode(self, new_node):
        if new_node in self.__node_list:
            raise ValueError('Trying to add two nodes with the same name')
        return True

    def addNode(self, **kwargs):
        new_node = Node(kwargs)
        if self.validateNode(new_node):
            self.__node_list.add(new_node)

    def validateLink(self, edge):
        if (edge.node1() not in self.__node_list) or (edge.node2() not in self.__node_list):
            raise ValueError('Trying to link non existent node')

        if not self.__allow_equal_edges:
            if edge in self.__edge_list:
                raise ValueError('Trying to create existent edge')

        return True

    def addLink(self, **kwargs):
        new_edge = Edge(kwargs)
        if self.validateLink(new_edge):
            self.__edge_list.add(new_edge)

    def dump(self, output_file=""):
        with open(output_file, 'w') as fl:
            f  = lambda k,v: "{} {}".format(k, v)

            node_header = "nodedef>" + ",".join( f(k,v) for k,v in Node.header().items() )
            fl.writelines(node_header)

            nodes = '\n' + "\n".join(str(node) for node in self.__node_list) + '\n'
            fl.writelines(nodes)

            edge_header = "edgedef>" + ",".join(f(k,v) for k,v in Edge.header().items() )
            fl.writelines(edge_header)

            edges = '\n' + "\n".join(str(edge) for edge in self.__edge_list)
            fl.writelines(edges)

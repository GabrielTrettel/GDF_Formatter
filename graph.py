#!/usr/bin/python3

class Node():
    def __init__(self, attr_dict):
        self.attributes = {key:value for key,value in attr_dict.items()}

    def __eq__(self, other):
        return self.attributes['name'] == other

    def __hash__(self):
        return hash(self.attributes['name'])

    def __str__(self):
        return ",".join(str(v) for v in self.attributes.values() )

    def usedAttributes():
        return self.attributes.keys()

class Edge():
    def __init__(self, attr_dict):
        self.attributes = {key:value for key,value in attr_dict.items()}

    def __eq__(self, node):
        return (self.attributes['node1'] != node) and (self.attributes['node2'] != node)

    def __hash__(self):
        return hash(self.attributes['node1']+self.attributes['node2']+str(self.attributes['weight']))

    def __str__(self):
        return ",".join(str(v) for v in self.attributes.values())

    def usedAttributes():
        return self.attributes.keys()

class Graph():
    def __init__(self, custom_node_attrs=dict(), custom_edge_attrs=dict(), allow_equal_edges=False, **kwargs):
        self.__allow_equal_edges = allow_equal_edges
        self.__used_node_parameters = set()
        self.__used_edge_parameters = set()
        self.__node_list = set()
        self.__edge_list = set()
        self.__node_header = { 'name':'VARCHAR',
                               'label':'VARCHAR',
                               'class':'VARCHAR',
                               'visible':'BOOLEAN',
                               'labelvisible':'BOOLEAN',
                               'width':'DOUBLE',
                               'height':'DOUBLE',
                               'x':'DOUBLE',
                               'y':'DOUBLE',
                               'color':'VARCHAR' }

        self.__edge_header = { 'node1':'VARCHAR',
                               'node2':'VARCHAR',
                               'weight':'DOUBLE',
                               'directed':'BOOLEAN',
                               'color':'VARCHAR' }
        self.__node_header.update(custom_node_attrs)
        self.__node_header.update(kwargs)
        self.__edge_header.update(custom_edge_attrs)


    def validateNode(self, inputs):
        if inputs['name'] in self.__node_list:
            raise ValueError('Trying to add two nodes with the same name')

        for attribute in inputs.keys():
            if attribute not in self.__node_header:
                raise ValueError('Trying to add a node with unidentified attributes')

        return True


    def addNode(self, **kwargs):
        if self.validateNode(kwargs):
            self.__node_list.add(Node(kwargs))
            self.__used_node_parameters.update(kwargs.keys())

    def validateEdge(self, inputs):
        if (inputs['node1'] not in self.__node_list) or (inputs['node2'] not in self.__node_list):
            raise ValueError('Trying to link non existent node')

        if not self.__allow_equal_edges:
            for edge in self.__edge_list:
                if inputs['node1'] == edge.attributes['node1'] and inputs['node2'] == edge.attributes['node2']:
                    raise ValueError('Trying to create existent edge')

        for attribute in inputs.keys():
            if attribute not in self.__edge_header:
                raise ValueError('Trying to add a edge with unidentified attributes')
        return True


    def addLink(self, **kwargs):
        if self.validateEdge(kwargs):
            self.__edge_list.add( Edge(kwargs) )
            self.__used_edge_parameters.update(kwargs.keys())

    def dump(self, output_file=""):
        with open(output_file, 'w') as fl:
            f = lambda k,r: "{} {}".format(k, r[k])
            cn = lambda key: key in self.__used_node_parameters
            ce = lambda key: key in self.__used_edge_parameters

            node_header = "nodedef>" + ",".join(f(k,self.__node_header) for k in self.__node_header if cn(k))
            fl.writelines(node_header)

            nodes = '\n' + "\n".join(str(node) for node in self.__node_list) + '\n'
            fl.writelines(nodes)

            edge_header = "\nedgedef>" + ",".join(f(k,self.__edge_header) for k in self.__edge_header if ce(k))
            fl.writelines(edge_header)

            edge = '\n' + "\n".join(str(node) for node in self.__edge_list)
            fl.writelines(edge)


if __name__ == "__main__":

    node = {'type':'VARCHAR', 'connections':'DOUBLE'}
    graph = Graph(custom_node_attrs=node, allow_equal_edges=True)

    graph.addNode(name='1', label='Foo', type='AP', connections=2)
    graph.addNode(name='2', label='Bar', type='cP', connections=2)
    graph.addNode(name='3', label='Qux', connections=4)

    graph.addLink(node1='1', node2='2', weight=0.3)
    graph.addLink(node1='2', node2='1', weight=0.4)
    graph.addLink(node1='1', node2='3', weight=0.1)

    graph.dump(output_file='saida.gdf')

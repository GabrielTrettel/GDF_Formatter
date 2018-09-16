#!/usr/bin/python3

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
            self.attributes = {key:value for key,value in attr_dict.items()}
            Node._used_node_attr.update(attr_dict.keys())

    def valid(self, attr_dict):
        for attribute in attr_dict.keys():
            if attribute not in Node._header:
                raise ValueError('Trying to add a node with unidentified attributes')
        return True

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.attributes['name'] == other.attributes['name']
        return self.attributes['name'] == other

    def __hash__(self):
        return hash(self.attributes['name'])

    def __str__(self):
        formatter = lambda key: str(self.attributes[key]) if key in self.attributes else ""
        return ",".join(formatter(key) for key in Node._header.keys() if key in Node._used_node_attr)

    @classmethod
    def update(cls, new_attr):
        Node._header.update(new_attr)

    @classmethod
    def header(cls):
        return {key:value for key,value in Node._header.items() if key in Node._used_node_attr}




class Edge():
    _used_edge_attr = set()
    _header = { 'node1':'VARCHAR',
                'node2':'VARCHAR',
                'weight':'DOUBLE',
                'directed':'BOOLEAN',
                'color':'VARCHAR' }

    def __init__(self, attr_dict):
        if self.valid(attr_dict):
            self.attributes = {key:value for key,value in attr_dict.items()}
            Edge._used_edge_attr.update(attr_dict.keys())

    def valid(self, attr_dict):
        for attribute in attr_dict.keys():
            if attribute not in Edge._header:
                raise ValueError('Trying to add a edge with unidentified attributes')
        return True

    def __eq__(self, node):
        return (self.attributes['node1'] != node.attributes['node1']) and (self.attributes['node2'] != node.attributes['node1'])

    def __hash__(self):
        return hash("".join(str(v) for v in self.attributes.values()))

    def __str__(self):
        formatter = lambda key: str(self.attributes[key]) if key in self.attributes else ""
        return ",".join(formatter(key) for key in Edge._header.keys() if key in Edge._used_edge_attr)

    @classmethod
    def update(cls, new_attr):
        Edge._header.update(new_attr)

    @classmethod
    def header(cls):
        return {key:value for key,value in Edge._header.items() if key in Edge._used_edge_attr}

    def node1(self):
        return self.attributes['node1']

    def node2(self):
        return self.attributes['node2']




class Graph():
    def __init__(self, custom_node_attrs=dict(), custom_edge_attrs=dict(), allow_equal_edges=False, **kwargs):
        self.__allow_equal_edges = allow_equal_edges
        self.__node_list = set()
        self.__edge_list = set()
        Node.update(custom_node_attrs)
        Edge.update(custom_edge_attrs)
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

            edge_header = "\nedgedef>" + ",".join(f(k,v) for k,v in Edge.header().items() )
            fl.writelines(edge_header)

            edges = '\n' + "\n".join(str(edge) for edge in self.__edge_list)
            fl.writelines(edges)


if __name__ == "__main__":

    node = {'type':'VARCHAR', 'connections':'DOUBLE'}
    edge = {'influence':'DOUBLE', 'weight':'DOUBLE'}
    graph = Graph(custom_node_attrs=node, custom_edge_attrs=edge, allow_equal_nodes=True)

    graph.addNode(name='1', label='Foo', type='t1', connections=2)
    graph.addNode(name='2', label='Bar', type='t1', connections=3)
    graph.addNode(name='3', label='Qux', connections=8)

    graph.addLink(node1='1', node2='2', weight=0.3)
    graph.addLink(node1='1', node2='2', weight=8, influence=8)
    graph.addLink(node1='2', node2='1', weight=0)
    graph.addLink(node1='2', node2='1', weight=0, influence=9)

    graph.dump(output_file='saida.gdf')

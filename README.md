# GDF Formatter

[![GitHub release](https://img.shields.io/github/release/GabrielTrettel/GDF_Formatter.svg)](https://github.com/GabrielTrettel/GDF_Formatter/releases)
[![PyPI](https://img.shields.io/pypi/v/gdf-formatter.svg)](https://pypi.org/project/gdf-formatter/)
[![AUR](https://img.shields.io/aur/version/python-gdf-formatter.svg)](https://aur.archlinux.org/packages/python-gdf-formatter/)
[![GitHub license](https://img.shields.io/github/license/GabrielTrettel/GDF_Formatter.svg)](https://github.com/GabrielTrettel/GDF_Formatter/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/gdf-formatter)](https://pepy.tech/project/gdf-formatter)

This is a simple and flexible Python library to create and format your graphs in GDF.

## Installation
You can install this package from [PyPi](https://pypi.org/project/gdf-formatter/)
```
pip install gdf-formatter
```

Or, for Arch systems, it's on [AUR](https://aur.archlinux.org/packages/python-gdf-formatter/) by installing ```python-gdf-formatter```.

## GDF format information

**GDF types:**

|    Type  |   Explanation     |
|:--------:|:-----------------:|
| VARCHAR  | A string          |
| BOOLEAN  | `true` or `false` |
| INTERGER | Interger number   |
| DOUBLE   | Float number      |

**Default Attributes:**

For nodes, the default GDF attributes are:

| Attribute    | Type     |
|:------------:|:--------:|
| name         | VARCHAR  |
| label        | VARCHAR  |
| class        | VARCHAR  |
| visible      | BOOLEAN  |
| labelvisible | BOOLEAN  |
| height       | DOUBLE   |
| x            | DOUBLE   |
| y            | DOUBLE   |
| width        | DOUBLE   |
| color        | VARCHAR  |

And for edges, the default GDF attributes are:

| Attribute    | Type     |
|:------------:|:--------:|
| node1        | VARCHAR  |
| node2        | VARCHAR  |
| weight       | DOUBLE   |
| directed     | BOOLEAN  |
| color        | VARCHAR  |

## How to use

**Importing the package**
```python
from gdf_formatter import Graph
```

**Declaring a graph:**

You have 3 different ways to declare a graph. The fist one is using the default constructor which implements the default attributes for GDF format as below

```python
graph = Graph()
```
You can also define custom nodes and edges attributes by passing a dictionary composed by `{attribute:type}` through the Graph constructor parameters `custom_nodes` and `custom_edges`

```python
node = {'type':'VARCHAR', 'connections':'DOUBLE', 'class':'DOUBLE'}
edge = {'influence':'DOUBLE', 'weight':'DOUBLE'}
graph = Graph(custom_nodes=node, custom_edges=edge)
```

Another way to do that is defining custom node attributes on the go as a parameter in the constructor as `name='TYPE'`, like that:

```python
graph = Graph(age='INTERGER')
graph2 = Graph(age='INTERGER', size='DOUBLE')
```

*Tips:*
 * You can use both dictionary and on-the-go methods at the same time
 * If you want to overwrite the type of a default attribute you can just pass them in one of the two way above

**Adding nodes:**

Only the `name` parameter are required
 ```python
 graph.addNode(name='1', label='Foo', type='t1', connections=2, age=80)
 ```

**Adding edges:**

Only the `node1` and `node2` parameters are required
```python
graph.addLink(node1='1', node2='2')
```

**Dumping a GDF formatted file:**
```python
graph.dump(output_file='output.gdf')
```

**Example**

```python
from gdf_formatter import Graph

node = {'type':'VARCHAR', 'connections':'DOUBLE'}
edge = {'influence':'DOUBLE', 'weight':'DOUBLE'}
graph = Graph(custom_nodes=node, custom_edges=edge, allow_equal_nodes=True, age='INTERGER')

graph.addNode(name='1', label='Foo', type='t1', connections=2, age=80)
graph.addNode(name='2', label='Bar', type='t1', connections=3)
graph.addNode(name='3', label='Qux', connections=8, age=21)

graph.addLink(node1='1', node2='2', weight=0.3)
graph.addLink(node1='1', node2='2', weight=8, influence=8)
graph.addLink(node1='2', node2='1', weight=0)
graph.addLink(node1='2', node2='1', weight=0, influence=9)

graph.dump(output_file='output.gdf')
```

**Example output**
```
nodedef>name VARCHAR,label VARCHAR,type VARCHAR,connections DOUBLE,age INTERGER
2,Bar,t1,3,
3,Qux,,8,21
1,Foo,t1,2,80
edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE,influence DOUBLE
2,1,0,9
1,2,8,8
2,1,0,
1,2,0.3,
```

## Credits

[GabrielTrettel](https://github.com/GabrielTrettel) for creating the library

[GrayJack](https://github.com/GrayJack) for creating the README

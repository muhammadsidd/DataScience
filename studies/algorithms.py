
class Node:

    def __init__(self, name):
        self.name = name
        self.connected = {}


class Edge:

    def __init__(self, node1, node2, weight):
        node1.connected[node2.name] = int(weight)
        node2.connected[node1.name] = int(weight)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
j = Node('J')
node_list = []
node_list.append(a)
node_list.append(b)
node_list.append(c)
node_list.append(d)
node_list.append(e)
node_list.append(f)
node_list.append(g)
node_list.append(h)
node_list.append(i)
node_list.append(j)


e1 = Edge(a, b, 5)
e2 = Edge(a, c, 4)
e3 = Edge(a, g, 10)
e4 = Edge(b, d, 4)
e5 = Edge(b, e, 2)
e6 = Edge(d, c, 1)
e7 = Edge(d, f, 2)
e8 = Edge(d, g, 6)
e9 = Edge(e, f, 3)
e10 = Edge(e, i, 4)
e11 = Edge(f, h, 2)
e12 = Edge(g, h, 6)
e13 = Edge(g, j, 9)
e14 = Edge(h, i, 1)
e15 = Edge(h, j, 3)
e16 = Edge(i, j, 3)

adj_list = {v: {} for v in node_list}

for node in adj_list:
    for (k,v) in node.connected.items():
        adj_list[node][k] = v

for k,v in adj_list.items():
    print("{}:{}".format(k.name, v))


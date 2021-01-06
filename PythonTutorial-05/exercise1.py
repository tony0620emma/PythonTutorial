class Edge():
    edges = []
    def __init__(self, distance, node1, node2):
        self.distance = distance
        self.node1 = node1
        self.node2 = node2
        node1.edges.append(self)
        node2.edges.append(self)
        Edge.edges.append(self)

    def __str__(self):
        return "%d <-- %d --> %d" % (self.node1.value, self.distance, self.node2.value)

class Node():
    nodes = []
    def __init__(self, value):
        self.value = value
        self.edges = []
        Node.nodes.append(self)

    def __str__(self):
        return "Node %d" % (self.value)

    @classmethod
    def get_node(self, value):
        for node in Node.nodes:
            if node.value == value:
                return node
        return None

if __name__ == '__main__':
    f = open("network.txt")
    edges = []
    nodes = []
    for line in f.readlines():
        distance = int(line.split(":")[1])
        pair = line.split(":")[0]
        value1 = int(pair.split(",")[0])
        value2 = int(pair.split(",")[1])
        print(value1, value2, distance)

        node1 = Node.get_node(value1)
        if not node1:
            node1 = Node(value1)
        node2 = Node.get_node(value2)
        if not node2:
            node2 = Node(value2)

        edge = Edge(distance, node1, node2)

    for edge in Edge.edges:
        print (edge)

    for node in Node.nodes:
        print (node)


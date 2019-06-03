class Graph(object):
    def __init__(self, Gdict=None):
        if Gdict is None:
            Gdict={}
        self.Gdict=Gdict
    def vertices(self):
        return list(self.Gdict.keys())
    def edges(self):
        return self.genedge()
    def addVertex(self,vertex):
        if vertex not in self.Gdict:
            self.Gdict[vertex]=[]
    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.Gdict:
            self.Gdict[vertex1].append(vertex2)
        else:
            self.Gdict[vertex1] = [vertex2]
    def genedge(self):
        edges=[]
        for vertex in self.Gdict:
            for neighbour in self.Gdict[vertex]:
                if {neighbour,vertex} not in edges:
                    edges.append({vertex,neighbour})
        return edges

if __name__ == '__main__':
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }
    graph=Graph(g)
    print(graph.vertices())
    print(graph.edges())
    graph.add_edge({"f","b"})
    graph.addVertex("M")
    graph.add_edge({"f","M"})
    print(graph.vertices())
    print(graph.edges())


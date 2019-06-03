
from collections import defaultdict
class Graph:
    def __init__(self,vertice):
        self.V=vertice
        self.graph=defaultdict(list)
        self.tc=[[0 for j in range(self.V)] for i in range(self.V)]
    def addedge(self,u,v):
        self.graph[u].append(v)

    def transclosure(self):
        for i in range(self.V):
            self.DFSU(i,i)
        print(self.tc)
    def DFSU(self,s,v):
        self.tc[s][v]=1


        for i in self.graph[v]:

            if self.tc[s][i]==0:

                self.DFSU(s,i)
if __name__ == '__main__':
    ver=int(input("Enter the number of vertices"))
    g=Graph(ver)
    c=True
    while c:
        arg=int(input("Enter your choice\n1.addedge\n2.Transitive Closure\n3.quit"))
        if arg==1:
            u=int(input("Enter the source vertice"))
            v=int(input("Enter the destination vertice"))
            g.addedge(u,v)
        elif arg==2:
            print("The Transitive Closure of the graph is")
            g.transclosure()
        elif arg==3:
            c=False
            continue
        else:
            print("Invalid argument")
    print(graph)

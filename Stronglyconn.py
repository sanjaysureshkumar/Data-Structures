from collections import defaultdict
class Graph:
    def __init__(self,vertice):
        self.V=vertice
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def DFSU(self,v,visited):
        visited[v]=True
        print(v,end=" ")
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSU(i,visited)
    def fillorder(self,v,visited,stack):
        visited[v]=True
        #print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillorder(i,visited,stack)
        stack=stack.append(v)
    def gettranspose(self):
        g=Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addedge(j,i)
        return g
    def PrintScc(self):
        stack=[]
        visited=[False]*self.V
        for i in range(self.V):
            if visited[i]==False:
                self.fillorder(i,visited,stack)
        gr=self.gettranspose()
        visited=[False]*self.V
        while stack:
            i=stack.pop()
            if visited[i]==False:
                gr.DFSU(i,visited)
                print("")


if __name__ == '__main__':
    '''ver=int(input("Enter the number of vertices"))
    g=Graph(ver)
    c=True
    while c:
        arg=int(input("Enter your choice\n1.addedge\n2.Transitive Closure\n3.quit"))
        if arg==1:
            u=int(input("Enter the source vertice"))
            v=int(input("Enter the destination vertice"))
            g.addedge(u,v)
        elif arg==2:
            print("The Strongly connected components of the graph are")
            g.PrintScc()
        elif arg==3:
            c=False
            continue
        else:
            print("Invalid argument")
    '''
    g=Graph(10)
    g.addedge(0,1)
    g.addedge(1,2)
    g.addedge(2,0)
    g.addedge(2,3)
    g.addedge(3,0)
    g.addedge(3,4)
    g.addedge(4,7)
    g.addedge(7,4)
    g.addedge(4,5)
    g.addedge(5,6)
    g.addedge(6,5)
    g.addedge(7,8)
    g.addedge(8,9)
    g.addedge(9,7)



    print ("Following are strongly connected components " +
                           "in given graph")
    g.PrintScc()


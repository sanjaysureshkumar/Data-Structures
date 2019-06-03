from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited=[False]*(100)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                visited[i]=True
    def DFS(self,v):

        visited = [False] * (v)
        for i in range(v):
            if visited[i]==False:
                self.DFSU(i,visited)
    def DFSU(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSU(i,visited)



if __name__ == '__main__':

    g=Graph()
    c=True
    while c:
        arg=int(input("Enter your choice\n1.Addedge\n2.BFS\n3.DFS\n4.quit"))
        if arg==1:
            src=int(input("Enter source"))
            dest =int(input("Enter destination"))
            g.addedge(src,dest)
        if arg==2:

            src=int(input("Enter source"))
            print("BFS of the graph is")
            g.BFS(src)
        if arg==3:
            m=int(input("Enter the number of vertices"))
            g.DFS(m)

        elif arg==4:
            c=False
            continue

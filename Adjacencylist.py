class Adj:
    def __init__(self,data):
        self.vertex=data
        self.next=None
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V
    def add_edge(self,src,dest):
        node=Adj(dest)
        node.next=self.graph[src]
        self.graph[src]=node
        node=Adj(src)
        node.next=self.graph[dest]
        self.graph[dest]=node
    def print_graph(self):
        for i in range(self.V):
            print("Adj list of vertex "+str(i)+" is",end=" ")
            temp=self.graph[i]
            while temp:
                print("-->"+str(temp.vertex),end=" ")
                temp=temp.next
            print("\n")
def SC(self,arg):
    if arg==1:
        src=int(input("Enter src"))
        dest=int(input("Enter dest"))
        self.add_edge(src,dest)
    if arg==2:
        self.print_graph()
if __name__ == '__main__':
    ver=int(input("Enter the number of vertices"))
    s=Graph(ver)
    c=True
    while c:
        print("Enter your choice\n 1.add_edge\n2.print graph\n3.quit")
        arg=int(input())
        if arg==3:
            c=False
            continue
        SC(s,arg)

from collections import defaultdict
def addedge(graph,u,v):
    graph[u].append(v)
def generateedge(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges
if __name__ == '__main__':
    graph=defaultdict(list)
    c=True
    while c:
        arg=int(input("Enter your choice\n1.addedge\n2.generateedge\n3.quit"))
        if arg==1:
            u=input("Enter the source vertice")
            v=input("Enter the destination vertice")
            addedge(graph,u,v)
        elif arg==2:
            print(generateedge(graph))
        elif arg==3:
            c=False
            continue
        else:
            print("Invalid argument")
    print(graph)

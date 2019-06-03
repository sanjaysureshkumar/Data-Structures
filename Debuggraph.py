def findpath(graph,u,v,path=[]):
    path.append(u)
    if u==v:
        return path
    for node in graph[u]:
        if node not in path:
            newpath=findpath(graph,node,v,path)
            if newpath:
                return newpath
    return None
def allpath(graph,u,v,path=[]):
    path.append(u)
    if u==v:
        return [path]
    paths=[]
    for node in graph[u]:
        if node not in path:
            newpath=allpath(graph,node,v,path)
        for new in newpath:
            paths.append(new)
    return paths
def shortestpath(graph,u,v,path=[]):
    path.append(u)
    if u==v:
        return [path]
    shortest=None
    for node in graph[u]:
        if node not in path:
            newpath=shortestpath(graph,node,v,path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest=newpath
    return shortest

if __name__ == '__main__':

    graph = { "a" : ["c"],
            "b" : ["c", "e"],
            "c" : ["a", "b", "d", "e"],
            "d" : ["c"],
            "e" : ["c", "b"],
            "f" : []
            }
    c=True
    while c:
        arg=int(input("Enter your choice\n1.print path\n2.print all path\n3.print shortest path\n4.quit"))
        if arg==1:
            src=input("Enter the source")
            dest=input("Enter the destination")
            print(findpath(graph,src,dest))
        elif arg==2:
            src=input("Enter the source")
            dest=input("Enter the destination")
            print(allpath(graph,src,dest))
        elif arg==3:
            src=input("Enter the source")
            dest=input("Enter the destination")
            print(shortestpath(graph,src,dest))
        elif arg==4:
            c=False
            continue
        else:
            print("Invalid argument")
    print(graph)

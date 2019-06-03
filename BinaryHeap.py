from heapq import heappush,heappop,heapify

class Minheap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    def insertkey(self,key):
        return heappush(self.heap,key)
    def decreasekey(self,i,newval):
        self.heap[i]=newval
        while (i!=0 and self.heap[self.parent(i)]>self.heap[i]):
            print(i)
            print(self.heap[i])
            print(self.heap[self.parent(i)])
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    def extractmin(self):
        return heappop(self.heap)
    def deletekey(self,i):

        self.decreasekey(i,float("-inf"))
        self.extractmin()
    def getmin(self):
        return self.heap[0]
    def printheap(self):
        length=len(self.heap)
        for i in range(length):
            print(self.heap[i])
def Switchcase(self,arg):
    if arg==1:
        key=int(input("Enter the key you want to insert"))
        self.insertkey(key)
        self.printheap()
    elif arg==2:
        if self==None:
            print("Heap is empty")
        else:
            pos=int(input("Enter the position you want to delete"))
            self.deletekey(pos)
            self.printheap()
    elif arg==3:
        pos=int(input("Enter the position"))
        new=int(input("Enter the new key"))
        self.decreasekey(pos,new)
        self.printheap()
    elif arg==4:
        c=self.getmin()
        print("The minimum value in the heap is "+str(c))

if __name__ == '__main__':
    s=Minheap()
    c=True
    while c:
        print("Enter your choice\n1.Insert\n2.Delete\n3.Decreasekey\n4.Get Minimum\n5.Quit")
        arg=int(input())
        if arg==5:
            c=False
            continue
        Switchcase(s,arg)


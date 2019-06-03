class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next_node
    def setnext(self,new_next):
        self.next_node=new_next

class linkedlist(Node):
    def __init__(self,head=None):
        self.head=head
    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.getnext()
        return count
    def insert(self,data,pos):
        if pos==1:
            if self.head==None:
                self.head=Node(data,None)
            else:
                temp=self.head
                self.head=Node(data,temp)
        else:
            if pos==(self.size()+1):
                #print(self.size())
                #print(pos)
                current=self.head
                while current.next_node!=None:
                    current=current.getnext()
                new_node=Node(data,None)
                current.next_node=new_node

            elif pos<(self.size()+1):
                current=self.head
                for i in range(pos-1):
                    prev=current
                    current=current.getnext()
                prev.next_node=Node(data,current)
            else:
                print("Position is out of bounds")
    def printList(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next_node
if __name__ == '__main__':
    s=linkedlist()
    s.insert(10,1)
    #s.printList()
    s.insert(20,2)
    #s.printList()
    s.insert(30,2)
    #print(s.size())
    #s.printList()
    s.insert(40,3)
    #s.printList()
    s.insert(50,2)
    #s.printList()
    #print(s.size())
    s.insert(60,6)
    #s.printList()
    s.insert(80,8)
    s.printList()


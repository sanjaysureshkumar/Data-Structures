class Node(object):
    def __init__(self,data=None,next_node=None,prev_node=None):
        self.data=data
        self.next_node=next_node
        self.prev_node=prev_node
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next_node
    def getprev(self):
        return self.prev_node
    def setnext(self,new_next):
        self.next_node=new_next
    def setprev(self,new_prev):
        self.prev_node=new_prev

class Dlinkedlist(Node):
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
                self.head=Node(data,None,None)
            else:
                temp=self.head
                self.head=Node(data,temp,None)
        else:
            if pos==(self.size()+1):
                current=self.head
                while current.next_node!=None:
                    current=current.getnext()
                new_node=Node(data,None,current)
                current.next_node=new_node

            elif pos<(self.size()+1):
                current=self.head
                for i in range(pos-1):
                    current=current.getnext()
                temp=current.prev_node
                new_node=Node(data,current,temp)
                temp.next_node=new_node
                current.prev_node=new_node
            else:
                print("Position is out of bounds")
    def printList(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next_node
if __name__ == '__main__':
    s=Dlinkedlist()
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


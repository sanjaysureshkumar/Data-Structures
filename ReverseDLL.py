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
        temp=Node(None,None,None)
        if pos==1:
            if self.head==None:
                self.head=Node(data,None,None)
            else:
                temp=self.head
                self.head=Node(data,temp,None)
                temp.prev=self.head
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
                new_node=Node(data,current,None)
                temp=current.prev_node
                current.prev_node=new_node
                temp.next_node=new_node
                new_node.prev_node=temp

            else:
                print("Position is out of bounds")
    def printList(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            #prev=current
            current=current.next_node

    def rev(self):
        temp=Node(None,None,None)
        current=self.head
        #print(current.data)
        while current:
            temp = current.prev_node
            current.prev_node = current.next_node
            current.next_node = temp
            current = current.prev_node
        self.head=temp.prev_node
        #print(temp.data)
def Switchcase(self,arg):
    if arg==1:
        data=input("Enter the data")
        pos=int(input("Enter the position"))
        self.insert(data,pos)
    elif arg==2:
        self.rev()
    elif arg==3:
        self.printList()
if __name__ == '__main__':
    s=Dlinkedlist()
    c=True
    while c:
        print("Enter your choice\n1.insert\n2.reverse\n3.print\n4.quit")
        arg=int(input())
        if arg==4:
            c=False
            continue
        Switchcase(s,arg)

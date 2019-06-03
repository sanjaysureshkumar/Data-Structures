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

    def findMergeNode(self, a):
        count1 = 0
        count2 = 0
        current = self.head
        while current:
            count1 += 1
            current = current.next_node
        current = a.head
        while current:
            count2 += 1
            current = current.next_node
        count = abs(count1 - count2)
        if count1 > count2:
            for i in range(count):
                self.head = self.head.next_node
        elif count1 < count2:
            for i in range(count):
                a.head = a.head.next_node
        current1 = self.head
        current2 = a.head
        while current1!=current2:
            #print(current1.data)
            #print(current2.data)
            current1 = current1.next_node
            current2 = current2.next_node
        print(current1.data)

    def merge(self,a,pos):
        current1=a.head
        while current1.next_node!=None:
            current1=current1.next_node
        current=self.head
        for i in range(pos-1):
            current=current.next_node
        current1.next_node=current

if __name__ == '__main__':
    s=linkedlist(10)
    a=linkedlist(10)
    s.insert(1,1)
    #s.printList()
    s.insert(2,2)
    #s.printList()
    s.insert(3,3)
    #s.insert(35,4)
    #print(s.size())
    #s.printList()
    a.insert(1,1)
    #s.printList()
    #a.insert(50,2)
    #s.printList()
    #print(s.size())
    #a.insert(60,3)
    #s.printList()
    #s.insert(80,8)
    #s.printList()
    s.merge(a,3)
    s.printList()
    print()
    a.printList()
    s.findMergeNode(a)



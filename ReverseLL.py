from Linkedlist import Node
from Linkedlist import linkedlist

def rev(s):
    current=s.head
    prev=None
    while current:
        temp=current.next_node
        current.next_node=prev
        prev=current
        current=temp
    s.head=prev

if __name__ == '__main__':
    s=linkedlist()
    '''
    c=True
    while c:
        print("Enter your choice\n1.insert\n2.reverse\n3.print\n4.quit")
        arg=int(input())
        if arg==4:
            c=False
            continue
        '''
    s.insert(10,1)
    #s.printList()
    s.insert(20,1)
    s.insert(30,2)
    s.insert(40,4)
    s.printList()
    rev(s)
    s.printList()




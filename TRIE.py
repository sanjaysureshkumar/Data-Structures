class Node(object):
    def __init__(self):
        self.children=[None]*26
        self.isEOW=False
class Trie(object):
    def __init__(self):
        self.root=self.getnode()
    def getnode(self):
        return Node()
    def chartoindex(self,ch):
        return ord(ch)-ord("a")
    def insert(self,str):
        PC=self.root
        length=len(str)
        for i in range(length):
            index=self.chartoindex(str[i])
            if not PC.children[index]:
                PC.children[index]=self.getnode()
            PC=PC.children[index]
        PC.isEOW=True
    def search(self,str):
        PC=self.root
        length=len(str)
        for i in range(length):
            index=self.chartoindex(str[i])
            if not PC.children[index]:
                return False
            PC=PC.children[index]
        return PC!=None and PC.isEOW
    def delete(self,str):
        PC=self.root
        length=len(str)
        for i in range(length):
            index=self.chartoindex(str[i])
            if not PC:
                print("Word not found")
                return -1
            PC=PC.children[index]
        if not PC:
            print("Word not found")
            return -1
        else:
            PC.isEOW=False
            return 0


    def isempty(self):
        for i in range(26):
            if self.children[i]!=None:
                return False
        return True

def Switchcase(self,arg):
    if arg==1:
        str=input("Enter the string you want to insert")
        str=str.lower()
        print(str)
        self.insert(str)
    elif arg==2:
        str=input("Enter the string you want to search")
        str=str.lower()
        if self.search(str):
            print("String Found")
        else:
            print("String Not Found")
    elif arg==3:
        str=input("Enter the string you want to delete")
        str=str.lower()
        self.delete(str)
if __name__ == '__main__':
    s=Trie()
    c=True
    while c:
        print("Enter your choice\n1.insert\n2.search\n3.Delete\n5.quit")
        arg=int(input())
        if arg==4:
            c=False
            continue
        Switchcase(s,arg)

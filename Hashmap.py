class hashmap:
    def __init__(self,size):
        self.size=size
        self.map=[None]*self.size
    def gethash(self,key):
        hash=0
        for char in str(key):
            hash+=ord(char)
        return hash % self.size
    def add(self,key,value):
        keyhash=self.gethash(key)
        keyvalue=[key,value]
        if self.map[keyhash] is None:
            self.map[keyhash]=list([keyvalue])
            return True
        else:
            for pair in self.map[keyhash]:
                if pair[0]==key:
                    pair[1]=value
                    return True
            self.map[keyhash].append(keyvalue)
            return True
    def get(self,key):
        keyhash=self.gethash(key)
        if self.map[keyhash] is not None:
            for pair in self.map[keyhash]:
                if pair[0]==key:
                    return pair[1]
        return None
    def delete(self,key):
        keyhash=self.gethash(key)
        if self.map[keyhash] is None:
            return False
        else:
            for i in range(len(self.map[keyhash])):
                if self.map[keyhash][i][0]==key:
                    self.map[keyhash].pop(i)
                    return True
    def print1(self):
        for item in self.map:
            print(item)
def Switchcase(self,arg):
    if arg==1:
        key=input("Enter the key you want to insert")
        value=input("Enter the value you want to insert")
        self.add(key,value)
        self.print1()
    elif arg==2:
        if self==None:
            print("Heap is empty")
        else:
            key=input("Enter the key you want to delete")
            self.delete(key)
            self.print1()
    elif arg==3:
        new=input("Enter the key")
        self.get(new)
        self.print1()

if __name__ == '__main__':
    s=hashmap(6)
    c=True
    while c:
        print("Enter your choice\n1.Add\n2.Delete\n3.Get value\n4.Quit")
        arg=int(input())
        if arg==4:
            c=False
            continue
        Switchcase(s,arg)


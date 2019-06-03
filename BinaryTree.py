class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Binarytree:
    def __init__(self, root=None):
        self.root=root
    def insert(self,data):
        if self.root==None:
            self.root=Node(data,None,None)
        else:
            if self.left==None:
                self.left=Node(data,None,None)
            elif self.right==None:
                self.right=Node(data,None,None)
            else:
                self.left.insert(data)


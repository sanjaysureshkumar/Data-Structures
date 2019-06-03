class BinaryStree():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def insert(self, data):
        if self.data == data:
            return False  # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinaryStree(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BinaryStree(data)
                return True
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print(self.data)

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            # deleting node with one child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.rightChild = self.right.delete(temp.data)

        return self

    def search(self,data):
        if data==self.data:
            print("Data found")
        elif data < self.data and self.left==None:
            print("Data Not found")
        elif data > self.data and self.right==None:
            print("Data not found")
        elif data < self.data:
            self.left.search(data)
        elif data > self.data:
            self.right.search(data)
class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BinaryStree(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False
    def height(Self):
        if self is None:
            return 0
        else :
            # Compute the height of each subtree
            lheight = height(self.left)
            rheight = height(self.right)

            #Use the larger one
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1
    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
    def levelorder(self):
        h=height(self.root)
        for i in range(1,h+1):
            self.printlevel(i)
    def printlevel(self,level):
        if self.root is None:
            return
        if level==1:
            print(self.root.data)
        elif level>1:
            self.left.printlevel(level-1)
            self.right.printlevel(level-1)
def Switchcase(self,arg):
    if arg==1:
        data=int(input("\nEnter the data to be inserted"))
        self.insert(data)
    elif arg==2:
        data=int(input("\nEnter the data to be deleted"))
        self.delete(data)
    elif arg==3:
        data=int(input("\nEnter the data you want to search"))
        self.search(data)
    elif arg==4:
        self.inorder()
    elif arg==5:
        self.preorder()
    elif arg==6:
        self.postorder()
    elif arg==7:
        self.levelorder()
    else:
        print("Invalid Input")
if __name__ == '__main__':
    s=Tree()
    c=True
    while c:
        print("Enter your choice\n1.insert\n2.Delete\n3.search\n4.inorder\n5.preorder\n6.postorder\n7.levelorder\n8.quit")
        arg=int(input())
        if arg==8:
            c=False
            continue
        Switchcase(s,arg)



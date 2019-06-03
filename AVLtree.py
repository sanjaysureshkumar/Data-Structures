class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVLTree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)
    def preorder(self,root):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.left:
                self.left.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self,root):

        if self:
            if root.leftChild:
                self.inorder(root.leftChild)
            print(str(self.data), end = ' ')
            if root.rightChild:
                self.inorder(root,rightChild)

    def postorder(self):

        if self:
            if self.left:
                self.left.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class AVLTree(object):
    def __init__(self,root=None):
        self.root = root

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return self.root


    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.preorder()

    def inorder(self,root):
        print()
        if self.root is not None:
            print('Inorder: ')
            if self.root:
                if root.leftChild:
                    self.inorder(root.leftChild)
                print(str(self.root.data), end=' ')
                if root.rightChild:
                    self.inorder(root.rightChild)

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
def Switchcase(self,arg,root):
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
        self.inorder(root)
    elif arg==5:
        self.preorder(root)
    elif arg==6:
        self.postorder(root)
    else:
        print("Indataid Input")
if __name__ == '__main__':
    s=AVLTree()
    c=True

    while c:
        print("Enter your choice\n1.insert\n2.Delete\n3.search\n4.inorder\n5.preorder\n6.postorder\n7.quit")
        arg=int(input())
        if arg==7:
            c=False
            continue
        Switchcase(s,arg,root=None)




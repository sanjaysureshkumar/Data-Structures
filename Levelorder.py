def levelorder(self):

    h = height(self)
    for i in range(1, h + 1):
        printlevel(self,i)
def printlevel(self, level):
    if self.root is None:
        return
    if level == 1:
        print(self.root.data)
    elif level > 1:
        printlevel(self.left,level - 1)
        printlevel(self.right,level - 1)

def height(self):
    if self is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(self.left)
        rheight = height(self.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

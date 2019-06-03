class stack:
    def __init__(self):
        self.items=[]

    def Switchcase(self, arg):
        default = "Invalid Input"
        return getattr(self, 'case_' + str(arg), lambda: default)()

    def case_1(self):
        data=input("\nEnter the data: ")
        self.items.append(data)

    def case_2(self):
        if self.items==[]:
            print("\nStack is empty")
        else:
            c=self.items[-1]
            self.items.pop()
            print("The Popped element is "+c)
    def case_3(self):
        if self.items==[]:
            return None
        else:
            print("\nThe peeked element is "+str(self.items[-1]))


    def printStack(self):
        for i in self.items:
            print(i)

#if __name__ == '__main__':
s=stack()
clk=True
while clk:
    arg=int(input("Enter Your choice 1.push\n2.pop\n3.peek\n4.quit"))
    if arg==4:
        clk=False
        continue
    s.Switchcase(arg)
        #print("The current elements of the stack is ")
    s.printStack()




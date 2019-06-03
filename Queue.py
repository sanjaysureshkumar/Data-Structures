class Queue:
    def __init__(self,capacity):
        self.front=self.size=0
        self.rear=capacity-1
        self.Q=[None]*capacity
        self.capacity=capacity

    def Switchcase(self, arg):
        return getattr(self, 'case_' + str(arg), lambda: default)()

    def case_1(self):
        item=input()
        if self.size==self.capacity:
            print("Queue is full")
        else:
            self.rear=(self.rear+1) % self.capacity
            self.Q[self.rear]=item
            self.size+=1


    def case_2(self):
        if self.size==0:
            print("Queue is empty")
        else:
            for i in range(self.capacity-1):
                self.Q[i]=self.Q[i+1]
            self.size-=1
            self.rear-=1
    def case_3(self):
        print("The front and rear element is")
        print(str(self.Q[self.front])+" and "+str(self.Q[self.rear]))
    def printQueue(self):
        for i in self.Q:
            print(i)
if __name__ == '__main__':
    q=Queue(5)
    c=True
    while c:
        print("Enter your choice \n1.Enqueue\n2.Dequeue\n3.Peek front and rear")
        arg=int(input())
        if arg>3 or arg<1:
            c=False
            continue
        q.Switchcase(arg)
        q.printQueue()

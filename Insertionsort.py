def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=(i-1)
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the number of elements\n"))
    for i in range(0,n):
        ele=int(input("Enter the "+str(i+1)+" th element\n"))
        arr.append(ele)

    insertionsort(arr)

    printList(arr)

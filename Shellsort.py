def shellsort(arr):
    n=len(arr)
    gap=n//2

    while gap>0:

        for i in range(gap,n):
            temp=arr[i]
            j=i

            while j>=gap and arr[j-gap]>temp:
                arr[j-gap]=arr[j]
                j-=gap
            arr[j]=temp
        gap/=2

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

    shellsort(arr)

    printList(arr)

def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)

        quicksort(arr,0,pivot-1)
        quicksort(arr,pivot+1,high)

def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[high],arr[i+1]=arr[i+1],arr[high]
    return (i+1)

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

    quicksort(arr,0,n-1)

    printList(arr)

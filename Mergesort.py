def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1

def printl(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the number of elements\n"))
    for i in range(0,n):
        ele=int(input("Enter the "+str(i+1)+" th element\n"))
        arr.append(ele)
    printl(arr)
    mergesort(arr)
    printl(arr)

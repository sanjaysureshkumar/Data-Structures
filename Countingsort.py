def countingsort(arr,max):
    c=[0]*(max+1)

    for i in range(len(arr)):
        c[arr[i]]=c[arr[i]]+1

    for j in range(1,max+1):
        c[j]=c[j]+c[j-1]
    result=[0]*(len(arr)+1)

    for k in reversed(arr):
        result[c[k]]=k
        c[k]=c[k]-1
    return result

def printl(arr):
    for i in range(1,len(arr)):
        print(arr[i],end=" ")
    print()

if __name__=='__main__':
    arr=[]
    n=int(input("Enter the number of elements\n"))
    for i in range(0,n):
        ele=int(input("Enter the "+str(i+1)+" th element\n"))
        arr.append(ele)

    max=arr[0]
    for j in range(1,len(arr)):
        if arr[j]>max:
            max=arr[j]

    Sorted_arr=countingsort(arr,max)
    printl(Sorted_arr)

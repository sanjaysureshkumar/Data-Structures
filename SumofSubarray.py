def SumofSubarr(arr,sum):
    n=len(arr)
    curr_sum=arr[0]
    start=0
    for i in range(1,n,1):
        while curr_sum>sum and start<(i-1):
            curr_sum-=arr[start]
            start+=1
        if curr_sum==sum:
            printL(arr,start,i)
            return 0
        if i<n:
            curr_sum+=arr[i]
    print("\nNo Subarray found")
    return 0

def printL(arr,start,k):
    result=[]
    for i in range(start,k):
        result.append(arr[i])
    print("\nThe Subarray with tha given sum is")
    print(result)

if __name__ == '__main__':
    lst=[]
    n=int(input("Enter the number of elements\n"))
    for i in range(0,n):
        ele=int(input("Enter the "+str(i)+" th element\n"))
        lst.append(ele)
    sum=int(input("Enter the sum"))
    SumofSubarr(lst,sum)

lst=[]
n=int(input("Enter the number of elements\n"))
for i in range(0,n):
    ele=int(input("Enter the "+str(i)+" th element\n"))
    lst.append(ele)
for i in range(0,n-1):
    min=lst[i]
    loc=i
    for k in range(i,n):
        if lst[k]< min :
            min=lst[k]
            loc=k
    temp=lst[i]
    lst[i]=lst[loc]
    lst[loc]=temp
print(lst)

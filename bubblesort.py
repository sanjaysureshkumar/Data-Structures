lst=[]
n=int(input("Enter the number of elements\n"))
for i in range(0,n):
    ele=int(input("Enter the "+str(i)+" th element\n"))
    lst.append(ele)
for i in range(0,n):
    for j in range(i+1,n):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)


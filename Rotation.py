if __name__ == '__main__':
    R=int(input())
    C=int(input())

    arr=[]
    for i in range(R):
        ele=int(input())
        arr.append(ele)
    ele=arr[0]
    k=[0]*(C)
    for i in range(C):
        k[i]=arr[i]
    for i in range(C,R):
        m=(i-C)%R
        #print(m)
        arr[m]=arr[i]
        #print(arr)
    for i in range(C):
        m=(i-C)%R
        arr[m]=k[i]
    for i in range(R):
        print(arr[i],end=" ")


def Spiralprint(n,m,matrix):
    i=l=k=0

    while l<n and k<m :
        for i in range(l,m):
            print(matrix[k][i],end=" ")
        k+=1
        for i in range(k,n):
            print(matrix[i][m-1],end=" ")
        m-=1
        if k<n:
            for i in range(m-1,l-1,-1):
                print(matrix[n-1][i],end=" ")
            n-=1
        if l<m:
            for i in range(n-1,k-1,-1):
                print(matrix[i][l],end=" ")
            l+=1


if __name__ == '__main__':
    R=int(input("Enter the number of rows: "))
    C=int(input("\nEnter the number of columns: "))
    print()
    matrix=[]
    for i in range(R):
        a=[]
        for j in range(C):
            a.append(int(input("")))
        matrix.append(a)

    Spiralprint(R,C,matrix)

import numpy as np

def FindK(n,m,matrix,k):

    if k<=m:
        print(matrix[0][k-1])
    elif k<=(m+n-1):
        print(matrix[k-m][m-1])
    elif k<=(2*m+n-2):
        print(matrix[n-1][m-1-(k-(m+n-1))])
    elif k<=(2*m+2*n-4):
        print(matrix[n-1-(k-(2*m+n-2))][0])
    else:
        matrix=innermatix(n,m,matrix)
        FindK(n-2,m-2,matrix,k-(2*m+2*n-4))

def innermatix(n,m,matrix):
    result=np.zeros((n-2,m-2))
    for i in range(1,n-1):
        for j in range(1,m-1):
            result[i-1][j-1]=matrix[i][j]
    return result

if __name__ == '__main__':
    R=int(input("Enter the number of rows: "))
    C=int(input("\nEnter the number of columns: "))
    print()
    matrix=[]
    for i in range(R):
        a=[]
        for j in range(C):
            a.append(int(input()))
        matrix.append(a)

    P=int(input("Enter the postion of the element"))
    print()

    FindK(R,C,matrix,P)

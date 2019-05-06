import numpy as np

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
    result=np.zeros((C,R))
    for i in range(R):
        for j in range(C):
            result[j][i]=matrix[i][j]

    for i in range(C):
        for j in range(R):
            print(result[i][j],end=" ")
        print()

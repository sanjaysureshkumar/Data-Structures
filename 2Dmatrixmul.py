import numpy as np

if __name__=='__main__':

    R1=int(input("Enter the number of rows of matrix 1: "))
    C1=int(input("\nEnter the number of columns of matrix 1: "))

    R2=int(input("\nEnter the number of rows of matrix 2: "))
    C2=int(input("\nEnter the number of columns of matrix 2: "))

    if R2!=C1 :
        print("\nInvalid matrix sizes.\nMultiplication cannot be carried out")
    else:
        matrix1=[]
        matrix2=[]

        print("\nEnter the elements of matrix 1: ")
        for i in range(R1):
            a=[]
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)

        print("\nEnter the elements of matrix 2: ")
        for i in range(R2):
            a=[]
            for j in range(C2):
                a.append(int(input()))
            matrix2.append(a)

        result=np.zeros((R1,C2))

        for i in range(R1):
            for j in range(C2):
                for k in range(C1):
                    result[i][j]+=matrix1[i][k]*matrix2[k][j]

        for i in range(R1):
            for j in range(C2):
                print(result[i][j],end=" ")
            print()

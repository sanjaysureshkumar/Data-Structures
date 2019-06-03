from math import *
def listprime(n):
    count=1
    prime=[2]

    for i in range(3,n,2):
        isprime=1
        jmax=int(sqrt(i))
        for j in range(3,jmax+1,2):
            if i%j==0:
                isprime=0
                break
        if isprime:
            prime.append(i)
            count+=1
    for k in range(count):
        print(prime[k])
def gethighprime(n):
    if n%2==0:
        n=n-1
    else:
        n=n-2
    for i in range(n,3,-2):
        isprime=1
        jmax=int(sqrt(i))
        for j in range(3,jmax+1,2):
            if i%j==0:
                isprime=0
                break
        if isprime:
            break
    return i
def computehashindex(ele,prime,j,n):
    hash1=ele%n
    hash2=prime-(ele%prime)
    c=(hash1+(j*hash2))% n
    print(c)
    return c

if __name__ == '__main__':
    n=int(input("Enter the size of the hash table"))
    hash=[None]*n
    #listprime(n)
    prime=gethighprime(n)
    print(prime)
    m=int(input("Enter the number of array elements"))
    print("Enter the array elements")
    a=[]
    for i in range(m):
        ele=int(input())
        a.append(ele)
    i=0
    for i in range(m):
        for j in range(n):
            index=computehashindex(a[i],prime,j,n)
            if hash[index]!=None:
                continue
            else:
                break
        hash[index]=a[i]
    for i in range(n):
        print(hash[i],end=" ")


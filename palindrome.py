if __name__ == '__main__':
    T=int(input())
    for k in range(T):
        Str=input()
        flag=0
        for i in range(len(Str)//2):
            if Str[i]!=str[n-i]:
                flag=1
                break;
        if flag==0:
            print("Yes\n")
        else:
            print("No\n")

T=int(input())
for i in range(0,T,1):
    flag=0
    k=0
    stack=[]
    str=input()
    if str[0]==")" or str[0]=="]" or str[0]=="}":
        flag=1
    else:
        for j in str:
            if j=="(" or j=="[" or j=="{":
                stack.append(j)
                k+=1
                #print(stack)
            elif j==")" and stack[k-1]=="(":
                stack.pop()
                #print(stack)
            elif j=="}" and stack[k-1]=="{":
                stack.pop()
                #print(stack)
            elif j=="]" and stack[k-1]=="[":
                stack.pop()
                #print(stack)
            else:
                flag=1
                #print(stack)
                break
        if len(stack)!=0:
            #print(stack)
            flag=1
    if flag==0:
        print("balanced")
    else:
        print("not balanced")

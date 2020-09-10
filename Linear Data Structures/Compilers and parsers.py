cases=int(input())
for _ in range(cases):
    stack,temp,tval,flag=0,0,0,0
    value=input()
    
    if value[0]=='>':
        print(0)
        continue
    for i in range(len(value)):
        if value[i]=='<':
            stack+=1
            temp+=1
        if value[i]=='>':
            stack-=1
            temp+=1
        if stack==0:
            tval=temp
        if stack<0:
            print(tval)
            flag=1
            break
    if flag!=1:
        print(tval)

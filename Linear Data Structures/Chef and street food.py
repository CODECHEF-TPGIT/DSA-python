test_cases=int(input())
for _ in range(test_cases):
    max_val=[]
    N=int(input())
    for _ in range(N):
        S,P,V=[int(x) for x in input().split()]
        cp=P//(S+1)
        cv=cp*V
        max_val.append(cv)
    print(max(max_val))
    

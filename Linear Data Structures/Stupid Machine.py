test_cases=int(input())
for _ in range(test_cases):
    tokens=0
    noc=int(input())
    values=list(map(int,input().split()))
    tokens+=(len(values))*min(values)
    ni=values.index(min(values))
    for i in values[:ni]:
        tokens+=(i-min(values))
    print(tokens)

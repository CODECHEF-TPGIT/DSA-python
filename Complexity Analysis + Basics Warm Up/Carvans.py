test_cases=int(input())
for i in range(test_cases):
    noc=int(input())
    cars=list(map(int,input().split()))
    count=0
    check=cars[0]
    for i in range(len(cars)):
        if cars[i]<=check:
            count+=1
            check=cars[i]
    print(count)

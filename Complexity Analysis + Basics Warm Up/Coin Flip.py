testcases=int(input())
coins=[]
for i in range(testcases):
    games=int(input())
    for j in range(games):
        I,G,Q = [int(x) for x in input().split()]
        if I==1:
            if G%2==0:
                print(G//2)
            else:
                H=G//2
                T=G-H
                if Q==1:
                    print(H)
                else:
                    print(T)
        else:
            if G%2==0:
                print(G//2)
            else:
                T=G//2
                H=G-T
                if Q==1:
                    print(H)
                else:
                    print(T)

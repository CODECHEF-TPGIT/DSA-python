test_cases=int(input())
for _ in range(test_cases):
    noc=int(input())
    number=list(input())
    ans=2*noc
    asc=0
    bsc=0
    alf=noc
    blf=noc
    for i in range (2*noc):
        if i%2==0:
            asc=asc+int(number[i])
            alf=alf-1
        else:
            bsc=bsc+int(number[i])
            blf=blf-1
        if asc>bsc+blf:
            ans=i+1
            break
        if bsc>asc+alf:
            ans=i+1
            break
    print(ans)

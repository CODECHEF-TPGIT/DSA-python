test_cases=int(input())
for _ in range(test_cases):
    laddus=0
    noc,con=input().split(maxsplit=1)
    for _ in range(int(noc)):
        contest=list(input().split())
        if contest[0]=="CONTEST_WON":
            laddus+=300
            if int(contest[1])<=20:
                laddus=laddus+(20-int(contest[1]))
        if contest[0]=="TOP_CONTRIBUTOR":
            laddus+=300
        if contest[0]=="BUG_FOUND":
            laddus+=int(contest[1])
        if contest[0]=="CONTEST_HOSTED":
            laddus+=50
    if laddus>=200 and con=="INDIAN":
        months=laddus//200
    elif laddus>=200 and con=="NON_INDIAN":
        months=laddus//400
    else:
        months=0 
    print(months)

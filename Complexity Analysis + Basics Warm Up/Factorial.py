count=int(input())
for i in range(count):
    value=int(input())
    noz=0
    power=1
    div=1
    while div!=0:
        div=value//pow(5,power)
        power+=1 
        noz+=div
    print(noz)
    noz=0

test_cases = int(input())
for _ in range(test_cases):
    arr = [int(num) for num in input().split()]
    k = arr[0]
    d0 = arr[1]
    d1 = arr[2]
    cycle = (2*(d0 + d1))%10 + (4*(d0 + d1))%10 + (8*(d0 + d1))%10 + (6*(d0 + d1))%10
    if k == 2:
        sum = d0 + d1
    else:
        sum = d0 + d1 + (d0 + d1)%10 + (((k-3)//4)*cycle)
        extra = ((k-3))% 4
        if extra == 1:
            sum += (2*(d0 + d1))%10
        elif extra == 2:
            sum += (2*(d0 + d1))%10 + (4*(d0 + d1))%10
        elif extra == 3:
            sum += (2*(d0 + d1))%10 + (4*(d0 + d1))%10 + (8*(d0 + d1))%10
    if (sum % 3) == 0:
        print("YES")
    else:
        print("NO")

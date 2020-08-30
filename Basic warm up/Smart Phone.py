count=int(input())
budget_list=[]
max_list=[]
max_value=0
for i in range(count):
    value=int (input())
    budget_list.append(value)
for a in range(len(budget_list)):
    for b in range(len(budget_list)):
        if budget_list[a]<=budget_list[b]:
            max_value+=budget_list[a]
    max_list.append(max_value)
    max_value=0
print(max(max_list))

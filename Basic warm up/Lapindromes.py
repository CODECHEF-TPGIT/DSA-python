from collections import Counter

def equality(dict1,dict2,fh):
    for a in fh:
        if dict2[a]!=dict1[a]:
            return False
    return True


count=int(input())


for i in range(count):
    string=str(input())

    if len(string)%2==0:
        mid=len(string)//2
        fh=string[:mid]
        frequency_fh = Counter(fh)
        sh=string[mid:]
        frequency_sh = Counter(sh)
        if fh==sh or equality(frequency_fh,frequency_sh,fh)  :
            print("YES")
        else:
            print("NO")
    else:
        mid=len(string)//2
        fh=string[:mid]
        frequency_fh = Counter(fh)
        sh=string[mid+1:]
        frequency_sh = Counter(sh)
        if fh==sh or equality(frequency_fh,frequency_sh,fh) :
            print("YES")
        else:
            print("NO")

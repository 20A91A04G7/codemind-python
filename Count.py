def even_odd_count(d):
    n=len(d)
    ec=0
    oc=0
    for i in d:
        if i%2:
            oc+=1
        else:
            ec+=1
    return ec,oc
n=int(input())
d=list(map(int,input().split()))
even,odd=even_odd_count(d)
print(even,odd)
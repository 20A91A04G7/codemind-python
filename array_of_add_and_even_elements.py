def even_odd(n):
    for i in range(n):
        c=d[i]
        if c%2!=0:
            print(c,end=' ')
    for i in range(n):
        c=d[i]
        if c%2==0:
            print(c,end=' ')
    return c
n=int(input())
d=list(map(int,input().split()))
count=even_odd(n)
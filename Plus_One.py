n=int(input())
a=list(map(int,input().split()))
c=0
r=0
for i in range(n):
    r=r*10+a[i]
r=r+1
t=r
while t:
    t//=10
    c+=1
if c>n:
    n=n+1
    a.append(0)
while(r):
    d=r%10
    a[n-1]=d
    r//=10
    n-=1
print(*a)
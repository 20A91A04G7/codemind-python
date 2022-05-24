n=int(input())
u=n**2
b=0
re=0
while n!=0:
    t=n%10
    b=b*10+t
    n=n//10
g=b**2
while g!=0:
    d=g%10
    re=re*10+d
    g=g//10
if(re==u):
    print("True")
else:
    print("False")
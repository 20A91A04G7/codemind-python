n=int(input())
length=len(str(n))
a=n
s=0
while a>0:
    d=a%10
    s=s+int(d**length)
    a=a//10
    length=length-1
if(s==n):
    print('True')
else:
    print('False')
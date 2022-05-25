n=int(input())
sum=0
for i in range(1,n+1):
    d=1/i
    i+=1
    sum=sum+d
print("%0.2f" %sum)
n=int(input())
arr=list(map(int,input().split()))
x=n//2
for i in range(n-1,x-1,-1):
    print(arr[i],end=" ")
for i in range(0,x):
    print(arr[i],end=" ")
for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        k=j%10
        if k==2 or k==3 or k==9:
            c+=1
    print(c)
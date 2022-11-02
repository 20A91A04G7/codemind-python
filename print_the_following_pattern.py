n=int(input())
for i in range(n):
    for j in range(n):
        if j==i:
            print('0',end="")
        else:
            print('x',end="")
    print()
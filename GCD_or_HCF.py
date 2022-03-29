N,M=map(int,input().split())
while M:
    if N>M:
        N,M=M,N
    M=M%N
print(N)
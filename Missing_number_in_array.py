def miss(arr,n):
    sumton=sum([i for i in range(1,n+1)])
    sumofarr=sum(arr)
    return sumton-sumofarr
t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(miss(arr,n))
m,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(m):
    for j in range(i+1,m+1):
        if sum(arr[i:j])==k:
            c+=1
print(c)
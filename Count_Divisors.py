i, j ,k=input().split()
m=int(i)
n=int(j)
div=int(k)
factors=[int(d) for d in range(m,n+1) if d%div==0]
print(len(factors))
        
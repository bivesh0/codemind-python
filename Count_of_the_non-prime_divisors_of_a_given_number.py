n=int(input())
factors=[int(x) for x in range(1,n+1) if n%x==0]
primes=[]
for i in factors:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c!=2:
       primes.append(i)
print(len(primes))        
        
        
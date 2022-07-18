n=int(input(""))
uglyprimes=[2,3,5]
if n==0:
    print("Not Ugly Number")
else:
    for i in uglyprimes:
        while n%i==0:
            n=n/i
            
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
    
    
    OR
    
    
n=int(input())
if n==0:
    print("Not Ugly Number")
elif n==1:
    print("Ugly Number")
else:
    uglyprimes=[2,3,5]
    factors=[int(x) for x in range(1,n) if n%x==0]
    primes=[]
    flag=0
    for i in range(1,n):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            primes.append(i)
 
    primefactors=[]
    for i in factors:
        if i in primes:
            primefactors.append(i)
    for i in primefactors:
        if i not in uglyprimes:
            flag+=1
            break
    if flag==0 and len(primefactors)>0:
        print("Ugly Number")
    else:
        print("Not Ugly Number")

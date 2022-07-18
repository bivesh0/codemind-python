def check(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=input()
rev=n[::-1]
count=check(int(n))
revcount=check(int(rev))
if revcount+count==2:
    print("circular prime")
elif revcount+count==1:
    print("prime but not a circular prime")
else:
    print("not prime")
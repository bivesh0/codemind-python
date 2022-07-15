def fact(n):
    fac=1
    for i in range(n,0,-1):
        fac=fac*i
    return fac    
n=int(input())
tmp=n
add=0
while n>0:
    rem=n%10
    f=fact(rem)
    add=add+f
    n//=10
if tmp==add:
    print("The number",tmp,"is a strong number")
else:
    print("The number",tmp,"is not a strong number")
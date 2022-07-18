n=int(input(""))
rev=0
if n>0:
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
else:
    res=0
    num=str(n)
    nonneg=num[1:]
    finalnum=int(nonneg)
    while finalnum>0:
        rem=finalnum%10
        res=res*10+rem
        finalnum//=10
    revstring='-'+str(res)
    rev=int(revstring)
print(rev)    
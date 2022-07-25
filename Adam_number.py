n=int(input())
sq1=n**2
nstr=str(n)
nrev=int(nstr[::-1])
sq2=nrev**2
sq2str=str(sq2)
sq2rev=int(sq2str[::-1])
if sq2rev==sq1:
    print("True")
else:
    print("False")
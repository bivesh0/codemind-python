numa=int(input(""))
afact=[int(x) for x in range(1,numa) if numa%x==0]
numb=int(input())
bfact=[int(x) for x in range(1,numb) if numb%x==0]
if sum(afact)==numb and sum(bfact)==numa:
    print("Amicable")
else:
    print("Not Amicable")

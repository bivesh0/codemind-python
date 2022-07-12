n=int(input(""))
factors=[int(x) for x in range(1,n) if n%x==0]
if sum(factors)>n:
    print("True")
else:
    print("False")
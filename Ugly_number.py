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
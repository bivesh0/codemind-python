def min(x,y):
    if x>y:
        return y
    else:
        return x
a, b=[int(x) for x in input().split()]
hcf=1
numa=int(a)
numb=int(b)
for i in range(1,min(a,b)+1): #min+1 because we have to iclude that number also
    if numa%i==0 and numb%i==0:
        hcf=i
print(hcf)        
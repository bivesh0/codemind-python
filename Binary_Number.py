def binaryn(n):
    binnum=""
    bun=str(n)
    while n>0:
        rem=n%2
        binnum=str(rem)+binnum
        n//=2
    return binnum  


n=int(input())
total=2**n
for i in range(total):
    binary=binaryn(i)
    if len(binary)!=n:
        print(str((n-len(binary))*'0')+binary)
    else:
        print(binary)
def check(num):
    sq=int(num**(1/2))
    mulp=int(sq*sq)
    if abs(mulp-num)==0:
        print("True")
    else:
        print("False")
n=int(input())
for i in range(n):
    check(int(input()))
    
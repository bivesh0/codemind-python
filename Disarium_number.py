def num(n):
    sum=0
    exp=1
    for i in n:
        sum=sum+int(i)**exp
        exp+=1
    return str(sum)
n=input()
operation=num(n)
if operation==n:
    print("True")
else:
    print("False")
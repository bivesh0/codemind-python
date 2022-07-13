def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
rep=int(input())
for i in range(rep):
    num=int(input(""))
    print(fact(num))
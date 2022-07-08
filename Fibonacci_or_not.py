n=int(input())
fib=[]
f1=0
f2=1
for i in range(15):
    f=f1+f2
    fib.append(f)
    f1=f2
    f2=f
if n in fib:
    print("True")
else:
    print("False")
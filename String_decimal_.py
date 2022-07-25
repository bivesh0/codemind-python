iter=int(input())
for k in range(iter):
    n=input()
    count=0
    l=len(n)
    for i in n:
        if i>='0' and i<='9':
            count+=1
    if count==l:
        print("True")
    else:
        print("False")
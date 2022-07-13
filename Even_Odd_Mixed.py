n=input("")
flag=0
for i in n:
    if int(i)%2==0:
        flag=flag
    else:
        flag+=1
if flag==len(n):
    print("Odd")
elif flag!=len(n) and flag>=1:
    print("Mixed")
else:
    print("Even")
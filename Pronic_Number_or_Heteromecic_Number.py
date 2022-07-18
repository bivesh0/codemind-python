num=int(input())
i=0
j=1
while i<=num:
    if(i*j==num):
        print("YES")
        break
    elif(i==num):
        print("NO")
        break
    i+=1
    j+=1
    
    
OR

n=int(input())
flag=0
for i in range(1,n+1):
    if i*(i+1)==n:
        flag+=1
        print("YES")
        break
if flag==0:
    print("NO")

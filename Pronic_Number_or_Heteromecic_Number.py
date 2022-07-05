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
    
    
    
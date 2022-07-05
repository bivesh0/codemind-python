a ,b=input().split()
num1=int(a)
num2=int(b)
i=1
while (i<=num1 and i<=num2):
    if(num1%i==0 and num2%i==0):
        hcf=i
    i+=1
lcm=(num1*num2)/hcf    
print(int(lcm))    
    
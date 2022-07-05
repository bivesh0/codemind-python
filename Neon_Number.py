number=input("")
sum=0
square=int(number)**2
for i in str(square):
    sum=sum+int(i)
if(sum==int(number)):
    print("Neon Number")
else:
    print("Not Neon Number")